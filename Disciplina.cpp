#include "Disciplina.h"

#include <iostream>
#include <stdlib.h>
#include <cstring>

using namespace std;

 Disciplina::Disciplina( char _den[], Profesor &p) : Profesor( p )
    {
        //de initializat ID-ul corect
        strcpy(denumire, _den);
    }
    int Disciplina::getIDDisc(void)
    {
        /*de completat*/
        return id_disc;
    }
    char* Disciplina::retNumeComplet(void)
    {
        /*de completat*/
        sprintf(_buff,"%s %s",Persoana::retNumeComplet(),denumire);
        return _buff;
    }
    char* Disciplina::retProfesor(void)
    {
        return Profesor::retNumeComplet();
    }
