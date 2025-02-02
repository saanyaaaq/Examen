#include "Student.h"

#include <iostream>
#include <stdlib.h>
#include <cstring>

using namespace std;
#include "Persoana.h"

Student::Student(Persoana &_pers, char _nr_mat[], char _spec[]):Persoana(_pers)
    {
        /*de completat*/
        strcpy(nr_mat,_nr_mat);
        strcpy(specializ,_spec);
    }
    char* Student::retNumeComplet(void)
    {
        /*de completat*/
        sprintf(_buff,"%s %s",Persoana::retNumeComplet(),specializ);
        return _buff;
    }
    char* Student::retNrMat(void)
    {
        /*de completat*/
        return nr_mat;
    }
    char* Student::retSpec(void)
    {
        /*de completat*/
        return specializ;
    }
