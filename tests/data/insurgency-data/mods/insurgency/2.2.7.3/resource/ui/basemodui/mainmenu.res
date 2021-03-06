"Resource/UI/MainMenu.res"
{
	"MainMenu"
	{
		"ControlName"				"Frame"
		"fieldName"					"MainMenu"
		"xpos"						"0"
		"ypos"						"0"
		"wide"						"5"		
		"tall"						"3"		
		"autoResize"				"0"
		"visible"					"1"
		"enabled"					"1"
		"tabPosition"				"0"
		"dialogstyle"				"1"
	}
					
	"BtnTestServerList"
	{
		"ControlName"				"BaseModHybridButton"
		"fieldName"					"BtnTestServerList"
		"xpos"						"0"
		"ypos"						"15"
		"wide"						"0"
		"tall"						"20"
		"autoResize"				"0"
		"visible"					"1"
		"enabled"					"1"
		"tabPosition"				"0"
		"navUp"						"BtnQuit"	
		"navDown"					"BtnFindAGame"
		"labelText"					"#INSURGENCY_MainMenu_TestServerListUI"
		"style"						"MainMenuButton"
		"command"					"OpenTestServerList"
		"ActivationType"			"1"
		"FocusDisabledBorderSize"	"1"
	}

	"BtnFindAGame"
	{
		"ControlName"				"BaseModHybridButton"
		"fieldName"					"BtnFindAGame"
		"xpos"						"0"
		"ypos"						"40"
		"wide"						"0"
		"tall"						"20"
		"autoResize"				"0"
		"visible"					"1"
		"enabled"					"0"
		"tabPosition"				"0"
		"navUp"						"BtnQuickGame"
		"navDown"					"BtnPlayWithFriends"
		"labelText"					"#INSURGENCY_MainMenu_FindGame"
		"style"						"MainMenuButton"
		"command"					"FindAGame"
		"ActivationType"			"1"
		"FocusDisabledBorderSize"	"1"
	}
	
	"BtnPlayWithFriends"
	{
		"ControlName"				"BaseModHybridButton"
		"fieldName"					"BtnPlayWithFriends"
		"xpos"						"0"
		"ypos"						"65"
		"wide"						"0"
		"tall"						"20"
		"autoResize"				"0"
		"visible"					"1"
		"enabled"					"0"
		"tabPosition"				"0"
		"navUp"						"BtnFindAGame"
		"navDown"					"BtnOptions"		
		"labelText"					"#INSURGENCY_MainMenu_PlayWithFriends"
		"style"						"MainMenuButton"
		"command"					"PlayWithFriends"
		"ActivationType"			"1"
	}

	"BtnOptions"
	{
		"ControlName"				"BaseModHybridButton"
		"fieldName"					"BtnOptions"
		"xpos"						"0"
		"ypos"						"90"
		"wide"						"0"
		"tall"						"20"
		"autoResize"				"0"
		"visible"					"1"
		"enabled"					"1"
		"tabPosition"				"0"
		"navUp"						"BtnPlayWithFriends"
		"navDown"					"BtnQuit"
		"labelText"					"#INSURGENCY_MainMenu_Options"
		"style"						"MainMenuButton"
		"command"					"Options"
		"ActivationType"			"1"
	}
	
	"BtnQuit" 
	{
		"ControlName"				"BaseModHybridButton"
		"fieldName"					"BtnQuit"
		"xpos"						"0"
		"ypos"						"115"
		"wide"						"0"
		"tall"						"20"
		"autoResize"				"0"
		"visible"					"1"
		"enabled"					"1"
		"tabPosition"				"0"
		"navUp"						"BtnOptions"
		"navDown"					"BtnQuickGame"
		"labelText"					"#INSURGENCY_MainMenu_QuitGame"
		"style"						"MainMenuButton"
		"command"					"QuitGame"
		"ActivationType"			"1"
	}
}
