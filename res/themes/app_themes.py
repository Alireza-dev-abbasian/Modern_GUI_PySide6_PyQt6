def setupStyleOne(themes):
    return f"""
    QWidget {{
        color: {themes["app_color"]["text_active"]};
        font: {themes["app_color"]["text_font"]};
    }}

    QToolTip {{
	    color: {themes["app_color"]["white"]};
	    background-color: {themes["app_color"]["bg_one"]};
	    background-image: none;
	    border: 1px solid {themes["app_color"]["gray"]};
        border-radius: 4px;
	    text-align: left;
	    padding: 3px;
    }}

    #bgApp {{
	    background-color: {themes["app_color"]["bg_one"]};
	    border: 1px solid {themes["app_color"]["bg_one"]};
        padding: 4px;
        border-radius: 8px;
    }}
    
    #titleLeftApp {{
        font: 60 12pt 'Segoe UI Semibold';
        color: {themes["app_color"]["text_title"]};
    }}

    #leftMenu {{
    	border-top: 1px solid {themes["app_color"]["gray"]};
    }}

    #leftMenuFrame {{
        background-color: {themes["app_color"]["dark_one"]};
        border-radius: 8px;
    }}

    #leftMenuTopFrame .QPushButton {{
    	background-position: left center;
        background-repeat: no-repeat;
    	border: none;
    	border-left: 20px solid transparent;
    	background-color: transparent;
    	text-align: left;
    	padding: 10 10 10 44 px;
    }}

    #leftMenuTopFrame .QPushButton:hover {{
    	background-color: {themes["app_color"]["dark_three"]};
    }}

    #leftMenuTopFrame .QPushButton:pressed {{
    	background-color: {themes["app_color"]["context_color"]};
    	color: {themes["app_color"]["white"]};
    }}

    #leftMenuBottomFrame .QPushButton {{
    	background-position: left center;
        background-repeat: no-repeat;
    	border: none;
    	border-left: 20px solid transparent;
    	background-color: transparent;
    	text-align: left;
    	padding-left: 44px;
    }}

    #leftMenuBottomFrame .QPushButton:hover {{
    	background-color: {themes["app_color"]["dark_three"]};
    }}

    #leftMenuBottomFrame .QPushButton:pressed {{
    	background-color: {themes["app_color"]["context_color"]};
    	color: {themes["app_color"]["white"]};
    }}

    #menu_button {{
    	background-position: left center;
        background-repeat: no-repeat;
    	border: none;
    	border-left: 20px solid transparent;
        background-image: url(:/icons/res/icons/icon_menu.svg);
    	text-align: left;
    	padding-left: 44px;
    	color: {themes["app_color"]["text_active"]};
    }}

    #menu_button:hover {{
    	background-color: {themes["app_color"]["dark_three"]};
    }}

    #menu_button:pressed {{
    	background-color: {themes["app_color"]["context_color"]};
    }}

    #btn_menu_home {{
        background-image: url(:/icons/res/icons/icon_home.svg);
    }}

    #btn_menu_settings {{
        background-image: url(:/icons/res/icons/icon_settings.svg);
    }}

    #btn_menu_info {{
        background-image: url(:/icons/res/icons/icon_info.svg);
    }}

    #content {{
        margin: 10 0 10 0 px;
    }}

    #contentTopTitle {{
       padding-left: 10px;
       font: {themes["app_color"]["text_font"]};
       color: {themes["app_color"]["text_title"]};
    }}

    #btn_connect {{
        background-color: {themes["app_color"]["green"]};
        color: {themes["app_color"]["white"]};
        border: none;
        border-style: solid;
        border-radius: 4px;
    }}

    #contentFrame {{
       margin: 2 2 2 10 px;
    }}

    #contentFrameTop {{
    	background-color: {themes["app_color"]["bg_two"]};
        border-radius: 8px;
    }}

    #contentTopButtonsFrame .QPushButton {{
        background-color: rgba(255, 255, 255, 0);
        border: none;
        border-radius: 5px;
    }}

    #btn_close:hover {{
        background-color: {themes["app_color"]["context_color"]};
        border-style: solid;
        border-radius: 4px;
    }}

    #btn_maximize_restore:hover {{
        background-color: {themes["app_color"]["bg_one"]};
        border-style: solid;
        border-radius: 4px;
    }}

    #btn_minimize:hover {{
        background-color: {themes["app_color"]["bg_one"]};
        border-style: solid;
        border-radius: 4px;
    }}

    #contentTopButtonsFrame .QPushButton:pressed {{
        background-color: {themes["app_color"]["gray"]};
        border-style: solid;
        border-radius: 4px;
    }}

    #rightBoxFrame {{
        background-color: {themes["app_color"]["dark_one"]};
        border-radius: 8px;
        padding: 10px;
    }}

    #bottomBar {{
    	background-color: {themes["app_color"]["bg_two"]};
        border-radius: 8px;
    }}

    #bottomBar QLabel {{
        font-size: 11px;
        color: {themes["app_color"]["text_foreground"]};
        padding-left: 10px;
        padding-right: 10px;
        padding-bottom: 2px;
    }}

    """
