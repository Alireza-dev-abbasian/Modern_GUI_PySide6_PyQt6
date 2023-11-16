def setupStyleOne(themes):
    return f"""
    QWidget {{
        color: {themes["app_color"]["text_active"]};
        font: {themes["app_color"]["text_font"]};
    }}

    QToolTip {{
	    color: #ffffff;
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

    #leftMenuFrame {{
        background-color: {themes["app_color"]["dark_one"]};
        border-radius: 8px;
    }}

    #titleLeftApp {{
        font: 60 12pt 'Segoe UI Semibold';
        color: {themes["app_color"]["text_title"]};
    }}

    #leftMenuTopFrame .QPushButton {{
    	background-position: left center;
        background-repeat: no-repeat;
    	border: none;
    	border-left: 15px solid transparent;
    	background-color: transparent;
    	text-align: left;
    	padding: 10 10 10 44 px;
        margin: 2px 0px 2px 4px;
    }}

    #leftMenuTopFrame .QPushButton:hover {{
    	background-color: {themes["app_color"]["dark_three"]};
    }}

    #leftMenuTopFrame .QPushButton:pressed {{
    	background-color: {themes["app_color"]["context_color"]};
    	color: #fff;
    }}

    #leftMenuBottomFrame .QPushButton {{
    	background-position: left center;
        background-repeat: no-repeat;
    	border: none;
    	border-left: 15px solid transparent;
    	background-color: transparent;
    	text-align: left;
    	padding-left: 44px;
        margin: 2px 0px 0px 4px;
    }}

    #leftMenuBottomFrame .QPushButton:hover {{
    	background-color: {themes["app_color"]["bg_one"]};
    }}

    #leftMenuBottomFrame .QPushButton:pressed {{
    	background-color: {themes["app_color"]["context_color"]};
    	color: #fff;
    }}

    #leftMenu {{
    	border-top: 1px solid {themes["app_color"]["gray"]};
    }}

    #leftMenuBottomFrame {{
    	background-color: {themes["app_color"]["dark_one"]};
    }}

    #toggleBox {{
        margin: 2px 0px 2px 4px;
    }}

    #menu_button {{
    	background-position: left center;
        background-repeat: no-repeat;
    	border: none;
    	border-left: 15px solid transparent;
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

    #contentTopTitle {{
       padding-left: 10px;
       font: {themes["app_color"]["text_font"]};
       color: {themes["app_color"]["text_title"]};
    }}

    #contentFrame{{
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

    #extraRightBox {{
        background-color: {themes["app_color"]["bg_one"]};
    }}

    #themeSettingsTopDetail {{
        background-color: rgb(189, 147, 249);
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
