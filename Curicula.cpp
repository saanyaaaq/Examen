#include "Curicula.h"

#include <iostream>
#include <stdlib.h>
#include <cstring>

using namespace std;
#include "Disciplina.h"

    Curicula::Curicula(char _spec[]) : N(0)
    {
        /* de tratat posibilele exceptii*/
        strcpy( den_specializ, _spec);
    }
    void Curicula::Add( int _sem, Disciplina &d, char _tip[] )
    {
        /* de tratat posibilele exceptii*/
        sem[N] = _sem;
        id_disc[N] = d.getIDDisc();
        strcpy( tip_disc[N], _tip );
        N++;
    }
