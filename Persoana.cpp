#include "Persoana.h"

#include <iostream>
#include <stdlib.h>
#include <cstring>

using namespace std;
#include "Persoana.h"

Persoana::Persoana( char _nume[], char _prenume[], char _data_n[])
    {
        /*de completat*/
         strcpy(nume,_nume);
         strcpy(prenume,_prenume);
         strcpy(data_n,_data_n);
    }
    char* Persoana::retDataNastere(void)
    {
        /*de completat*/
        return data_n;
    }
    char* Persoana::retNumeComplet(void)
    {
        /*de completat*/
        sprintf(_buff,"%s %s",nume,prenume);
        return _buff;
    }
    istream& operator>>(istream &c, Persoana &p)
    {
        /*de completat*/
        cout<<"Citire"<<endl;
        c>>p.nume>>p.prenume>>p.data_n;
        return c;
    }

