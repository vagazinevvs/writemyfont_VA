// lang_ko.js
// Defines all translatable text for the Korean interface
const translations = {
    // 介面標籤 (HTML 靜態內容)
    "title_main": "나만의 글꼴 생성기 by 字嗨",
    "label_wordlist": "문자표:",
    "dialog_char_list": "문자 목록",
    "dialog_hint_title": "팁 (Tip)",
    "settings_title": "설정",
    "download_title": "다운로드",
    "label_save_as_tester": "테스트 출력",
    "h3_download_font": "글꼴 다운로드",
    "interface_lan": "인터페이스 언어",
    "label_font_name_eng": "글꼴 영문 이름",
    "label_font_name_cjk": "글꼴 한글 이름",
    "label_scale_rate": "확대/축소율",
    "label_small_mode": "글씨가 정말 작음",
    "label_grid_style": "배경 격자 스타일",
    "label_no_fixed_width": "한글/한자 비균일 폭",
    "label_pressure_effect": "필압 감도 (실험 중)",
    "label_old_pressure": "구형 필압 모드 활성화 (권장하지 않음)",
    
    // Block Headers
    "h3_clear_all": "글꼴 데이터 전체 삭제",
    "h3_export_events": "시스템 이벤트 내보내기 (개발용)",
    "h3_import_data": "이전 백업 데이터 가져오기",
    "h3_export_data": "편집 중인 데이터 내보내기",

    // Export filter
    "label_export_filter": "내보내기 범위:",
    "option_export_all": "모든 문자 ALL",
    "option_export_zh_basic": "한자",
    "option_export_ko_basic": "한글 ",

    // Button Texts
    "button_clear_all_text": "글꼴 데이터 삭제 (복원 불가!)",
    "button_export_events_text": "시스템 이벤트 내보내기",
    "button_download_font_otf": "글꼴 OTF 파일 다운로드",
    "button_export_data_backup": "작업 중인 글꼴 데이터 백업",
    
    // Option Translations (Select Option Texts)
    "grid_3x3": "9분할 격자",
    "grid_3x3_new": "새 9분할 격자",
    "grid_2x2": "정사각형 격자",
    "grid_star": "미자격 (별모양)",
    "grid_box": "회자격 (되돌이)",
    "grid_no": "격자 없음 (글리프 박스만)",
    "option_none": "원시 값",
    "option_contrast": "대비 증가",
    "option_enhance": "강화 (노력 절감)",
    "option_enhancex": "추가 강화 (더 노력 절감)",
    
    // Hints and Notes (HTML <span class="note"> Content)
    "note_interface_lang": "앱의 표시 언어를 설정합니다. 변경 후 페이지가 자동으로 다시 로드됩니다.",
    "note_welcome": "글쓰기 전에 몇 가지 기본 정보를 설정해 봅시다! 이 설정들은 나중에 언제든지 변경할 수 있습니다.<br>앱 내장 브라우저에서 이 페이지를 열 경우 데이터 손실을 방지하기 위해 시스템 브라우저를 사용하는 것을 권장합니다!",
    "note_scale_rate": "손글씨를 쓸 때 틀을 벗어나지 않으려고 무의식적으로 글씨를 작게 쓰는 경향이 있습니다. 여기서 문자 칸의 크기를 조정할 수 있습니다.",
    "note_small_mode": "글씨가 정말 작은 분에게 적합합니다.",
    "note_no_fixed_width": "비균일 폭으로 설정하면 손글씨처럼 보이지만 세로 쓰기에는 적합하지 않을 수 있습니다.",
    "note_pressure_effect": "이 옵션은 필압 기능이 있는 장치에만 유효합니다. 현재 조정 중이며, 향후 변경 사항은 이전 버전과의 호환성을 유지하기 어려울 수 있습니다.",
    "note_old_pressure": "구형 필압 모드는 브러시 기능을 지원하지 않습니다.",
    "note_save_as_tester": "테스트 출력을 선택하면 글꼴 이름에 일련번호가 추가됩니다. 이는 시스템 캐시로 인해 컴퓨터에 정상적으로 설치되지 않는 문제를 방지합니다.",
    
    // fdrawer Internal Messages (For internal JS use)
    "fdrawer_font_name_cjk": "나의 손글씨",
    "fdrawer_find_msg": "찾을 문자를 입력하세요:",
    "fdrawer_not_found": "이 문자를 찾을 수 없습니다!",
    "fdrawer_confirm_add": "사용자 문자표에 추가하시겠습니까?",
    "fdrawer_no_data_export": "내보낼 수 있는 데이터가 없습니다.",
    "fdrawer_import_confirm": "데이터를 가져오시겠습니까? 현재 편집 중인 모든 데이터는 지워집니다.",
    "fdrawer_import_done": "가져오기가 완료되었습니다.",
    "fdrawer_clear_confirm": "작성된 모든 글꼴을 지우시겠습니까?",
    "fdrawer_clear_done": "지워졌습니다.",
    "fdrawer_welcome_title": "나만의 글꼴 생성기에 오신 것을 환영합니다!",
    "fdrawer_settings_title": "글꼴 설정",
    "fdrawer_in_app_notice": "최적의 사용 경험을 위해 기기 브라우저를 사용하는 것을 권장합니다.",
    "fdrawer_custom_list": "사용자 문자표",
	"fdrawer_import_confirm_incremental": "데이터를 가져오시겠습니까? 데이터베이스에 없는 문자만 추가되며, 이미 작성된 문자는 덮어쓰지 않습니다."
};