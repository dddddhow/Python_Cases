#include "TJU_SHEN_2019.h"

using namespace arma;

int main()
{

    int n1=15000;
    int n2=13061;
    arma::Mat<float> dat;
    dat.load("./vp_marmousi-ii_nt15000_nx13061_dt0.0002.dat",raw_binary);
    dat.reshape(n1,n2);

    for(int i1=0; i1<n1; i1++)
    {
        for(int i2=0; i2<n2; i2++)
        {
            if(dat(i1,i2)>=4700)
            {
                dat(i1,i2)=4700;
            }
            if(dat(i1,i2)<=1500)
            {
                dat(i1,i2)=1500;
            }
        }
    }

    dat.save("./vp_marmousi-ii_nt15000_nx13061_dt0.0002.dat",raw_binary);

    //arma::Mat<float> dat;
    //dat.load("./vp_marmousi-ii_nx13601_nz2801_dxdz_1.25m.dat",raw_binary);
    //dat=dat*1000;
    //dat.save("./vp_marmousi-ii_nx13601_nz2801_dxdz_1.25m.dat_new",raw_binary);


    return 0;
}
