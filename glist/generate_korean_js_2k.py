import math

def generate_korean_js(output_filename="korean_data_2350.js"):
    # --- 1. 準備資料容器 ---
    glyph_map_entries = []
    glyph_list_entries = {}
    common_hangul_list = []

    # --- 2. 處理韓文基礎字母 (Compatibility Jamo) ---
    # 範圍 U+3131 ~ U+3163 (ㄱ ~ ㅣ)
    jamo_list = []
    for code in range(0x3131, 0x3164):
        char = chr(code)
        key = f"uni{code:04X}"
        
        # 加入 Map
        glyph_map_entries.append(f'  \"{key}\": {{\"c\":\"{char}\",\"w\":\"F\"}}')
        jamo_list.append(key) # 儲存未加引號的鍵
    
    glyph_list_entries["韓文基礎字母"] = jamo_list

    # --- 3. 處理韓文常用 2350 字 (KS X 1001) ---
    # 限制從 U+AC00 開始的音節數量，以確保字元數量為 2350。
    DESIRED_COUNT = 2350
    END_CODE = 0xAC00 + DESIRED_COUNT
    
    for code in range(0xAC00, END_CODE):
        char = chr(code)
        key = f"uni{code:04X}"
        
        # 加入 Map
        glyph_map_entries.append(f'  \"{key}\": {{\"c\":\"{char}\",\"w\":\"F\"}}')
        common_hangul_list.append(key) # 儲存未加引號的鍵

    # --- 4. 將常用字分頁 (每頁 100 字) ---
    page_size = 100 
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
        
        # 修改列表名稱以反映新的分頁大小
        list_name = f"韓文常用字 {i+1:02d} [{first_char}-{last_char}]"
        
        # 儲存未加引號的鍵
        glyph_list_entries[list_name] = chunk 

    # --- 5. 輸出檔案內容 ---
    output_filename_2350 = output_filename
    
    js_content = "// 本檔案由 Python 腳本自動生成，包含韓文基礎字母與 KS X 1001 常用字\\n\\n"
    
    # 寫入 Map (擴充 glyphMap)
    js_content += "const koreanGlyphMap = {\n"
    js_content += ",\n".join(glyph_map_entries)
    js_content += "\n};\n\n"

    # 寫入 List (擴充 glyphList)
    js_content += "const koreanGlyphList = {\n"
    list_entries_str = []
    # 這裡將未加引號的鍵加上引號並 join
    for name, keys in glyph_list_entries.items():
        quoted_keys = [f'\"{k}\"' for k in keys]
        keys_str = ",".join(quoted_keys)
        list_entries_str.append(f'  \"{name}\": [{keys_str}]')
    
    js_content += ",\n".join(list_entries_str)
    js_content += "\n};\n\n"

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

    with open(output_filename_2350, "w", encoding="utf-8") as f:
        f.write(js_content)

    return (
        f"成功生成 {output_filename_2350}！"
    )

if __name__ == "__main__":
    generate_korean_js("korean_data_2350.js")