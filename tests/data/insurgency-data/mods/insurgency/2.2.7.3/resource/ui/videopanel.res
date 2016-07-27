"Resource/UI/VideoPanel.res"
{
	"class"
	{
		"ControlName"	"VideoPanel"
		"fieldName"		"videopanel"
		"xpos"			"0"
		"ypos"			"0"
		"wide"			"f0"
		"tall"			"f0"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"tabPosition"	"0"
	}

	"PnlGamerPic"
	{
		"ControlName"			"ImagePanel"
		"fieldName"				"PnlGamerPic"
		"xpos"					"1"
		"ypos"					"r41"
		"wide"					"40"
		"tall"					"40"
		"visible"				"0"
		"enabled"				"1"
		"tabPosition"			"0"
		"scaleImage"			"1"
		"image"					"icon_lobby"
		"usetitlesafe"			"1"
	}

	"LblGamerTag"
	{
		"ControlName"			"Label"
		"fieldName"				"LblGamerTag"
		"xpos"					"45"
		"ypos"					"r43"
		"wide"					"300"
		"tall"					"25"
		"visible"				"0"
		"enabled"				"1"
		"tabPosition"			"0"
		"Font"					"GamerTag"
		"labelText"				""
		"textAlignment"			"west"
		"fgcolor_override"		"255 255 255 255"
		"usetitlesafe"			"1"
		"noshortcutsyntax"		"1"
	}
	
	"LblGamerTagStatus"
	{
		"ControlName"			"Label"
		"fieldName"				"LblGamerTagStatus"
		"xpos"					"45"
		"ypos"					"r22"
		"wide"					"200"
		"tall"					"25"
		"visible"				"0"
		"enabled"				"1"
		"tabPosition"			"0"
		"Font"					"GamerTagStatus"
		"labelText"				"#PORTAL2_Coop_YourPartnerInScience"
		"textAlignment"			"west"
		"fgcolor_override"		"255 255 255 255"
		"usetitlesafe"			"1"
	}

	"WaitingForPlayers"
	{
		"ControlName"			"Label"
		"fieldName"				"WaitingForPlayers"
		"xpos"					"r300"
		"ypos"					"r22"
		"wide"					"300"
		"tall"					"25"
		"autoResize"			"0"
		"visible"				"0"
		"enabled"				"1"
		"tabPosition"			"0"
		"Font"					"GamerTagStatus"
		"labelText"				"#PORTAL2_Coop_WaitingForYourPartner"
		"textAlignment"			"east"
		"fgcolor_override"		"255 255 255 255"
		"usetitlesafe"			"1"
	}		
}