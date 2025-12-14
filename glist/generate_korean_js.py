import math

def generate_korean_js(output_filename="korean_data.js"):
    # --- 1. 準備資料容器 ---
    glyph_map_entries = []  # 存 "uniXXXX": {"c": "字", "w": "F"}
    glyph_list_entries = {} # 存分頁列表

    # --- 2. 處理韓文基礎字母 (Compatibility Jamo) ---
    # 範圍 U+3131 ~ U+3163 (ㄱ ~ ㅣ)
    jamo_list = []
    for code in range(0x3131, 0x3164):
        char = chr(code)
        key = f"uni{code:04X}"
        
        # 加入 Map
        glyph_map_entries.append(f'  "{key}": {{"c":"{char}","w":"F"}}')
        jamo_list.append(f'"{key}"')
    
    glyph_list_entries["韓文基礎字母"] = jamo_list

    # --- 3. 處理韓文常用 2350 字 (KS X 1001) ---
    # 利用 EUC-KR 編碼特性過濾常用字
    common_hangul_list = []
    
    # 韓文音節區塊 U+AC00 ~ U+D7A3
    for code in range(0xAC00, 0xD7A3 + 1):
        char = chr(code)
        try:
            char.encode('euc-kr') # 測試是否為常用字
            key = f"uni{code:04X}"
            
            # 加入 Map
            glyph_map_entries.append(f'  "{key}": {{"c":"{char}","w":"F"}}')
            common_hangul_list.append(key)
            
        except UnicodeEncodeError:
            continue

    # --- 4. 將常用字分頁 (每頁 100 字) ---
    page_size = 150
    total_pages = math.ceil(len(common_hangul_list) / page_size)

    for i in range(total_pages):
        start = i * page_size
        end = start + page_size
        chunk = common_hangul_list[start:end]
        
        # 取得該頁首尾字，做為標題提示
        first_code = int(chunk[0].replace("uni", ""), 16)
        last_code = int(chunk[-1].replace("uni", ""), 16)
        first_char = chr(first_code)
        last_char = chr(last_code)
        
        list_name = f"韓文-{i+1:02d} [{first_char}-{last_char}]"
        
        # 格式化為 JS 陣列字串
        quoted_keys = [f'"{k}"' for k in chunk]
        glyph_list_entries[list_name] = quoted_keys

    # --- 5. 輸出檔案內容 ---
    js_content = "// 本檔案由 Python 腳本自動生成，包含韓文基礎字母與 KS X 1001 常用字\n\n"
    
    # 寫入 Map (擴充 glyphMap)
    js_content += "const koreanGlyphMap = {\n"
    js_content += ",\n".join(glyph_map_entries)
    js_content += "\n};\n\n"

    # 寫入 List (擴充 glyphList)
    js_content += "const koreanGlyphList = {\n"
    for name, keys in glyph_list_entries.items():
        keys_str = ",".join(keys)
        js_content += f'  "{name}": [{keys_str}],\n'
    js_content += "};\n\n"

    # 寫入自動合併邏輯 (讓它能與原本的 cglyphlist.js 共存)
    js_content += """
// 將韓文資料合併到主資料中
if (typeof glyphMap !== 'undefined') {
    Object.assign(glyphMap, koreanGlyphMap);
}
if (typeof glyphList !== 'undefined') {
    Object.assign(glyphList, koreanGlyphList);
}
"""

    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(js_content)

    print(f"成功生成 {output_filename}！")
    print(f"共包含 {len(jamo_list)} 個基礎字母")
    print(f"共包含 {len(common_hangul_list)} 個常用音節字")

if __name__ == "__main__":
    generate_korean_js()