#include "TJU_SHEN_2019.h"

using namespace arma;
using namespace std;

int main()
{   int n1=2801*6;
    int n2=13601;
    float dt=0.0002;
    float df=1.0/dt/n1;


    arma::Mat<float>  dat;
    dat.load("./dat_in_new.dat",raw_binary);
    dat.reshape(n1,n2);

    //arma::Col<cx_float> dat_f(n1,fill::zeros);
    //for(int i2=n2/2-10; i2<n2/2+10; i2++)
    //{
        //cout<<"NO."<<i2+1<<"/"<<n2<<endl;
        //dat_f=dat_f+fft(dat.col(i2));
    //}

    //cout<<df<<endl;
    //arma::Col<float> dat_f_abs = abs(dat_f);
    //dat_f_abs.save("./dat_f_abs.sat",raw_binary);

    arma::Col<float> d=dat.col(n2/2);
    arma::Col<float> d_out(n1,fill::zeros);
    shen_choose_specific_band_1d(d,d_out,n1,dt,9,250);
    d.save("./d.dat",raw_binary);
    d_out.save("./d_out.dat",raw_binary);

    return 0;
}
