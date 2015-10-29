#include<iostream>  
#include<cstdlib> 
#include<fstream> 
using namespace std;  
int main(){  
ofstream fout("rollFile");
      for(int i=1;i<10000;i++)  
 fout<<rand()%100 + 12<<"\t"<< (rand()%15)*7 + 505 << "\t"<<rand()%10 + 1<<"\n";  
}
