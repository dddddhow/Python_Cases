//****************************************************************************//
// 测试实验 ： 为了说明 不同频率带的成分 对成像的影响                         //
//              这里主要是 0-2Hz  3-8Hz 9-60Hz                                //
//****************************************************************************//

#include <TJU_SHEN_2019.h>

using namespace std;
using namespace arma;


int main()
{

//============================================================================//
    cout<<"Step 1 : Parameters define & Data load"<<endl;
    int nz=750;
    int nz_new=nz*6;
    int nx=497;
    float dz=1.25;
    float dx=1.25;
    float dt=0.001;
    float df=1.0/dt*1.0/nz_new;

    float fre_min;
    float fre_max;

    int flag=4;

    if(flag==0) //0-3
    {
        fre_min = 0+df*3;
        fre_max = 3-df*3;
    }
    if(flag==1) //3-8
    {
        fre_min = 3+df*2;
        fre_max = 9-df*3;
    }
    if(flag==2) //8-60
    {
        fre_min = 9+df*4;
        fre_max = 60-df*3;
    }
    if(flag==3) //60-max
    {
        fre_min = 60+df*4;
        fre_max = df*nz*1.0/2-df*6;
    }
    if(flag==4) //9-35
    {
        fre_min = 9+df*4;
        fre_max = 35;
    }

    cout<<" "<<(fre_max-fre_min)*1.0/(df)<<endl;
    //pause();

    printf("    (n1,n2)               =>      (%8d,%8d)\n",nz,nx);
    printf("    (n1_new,n2_new)       =>      (%8d,%8d)\n",nz_new,nx);
    printf("    (d1,d2,dt)            =>      (%8.2fm,%8.2fm,%8.5fs)\n",dz,dx,dt);
    printf("    (df, f_nyquist)       =>      (%8.3fHz,%8.3fHz)\n",1/dt/nz_new,1/(dt*2));

    arma::Mat<float> dat_in;
    dat_in.load("./MiniMarmousi_nz750_nx497.dat",raw_binary); //时间域
    dat_in.reshape(nz,nx);
    //vel 2 impedance , rho=2000
    dat_in = dat_in*2000;
    dat_in.save("./dat_ampedance.dat",raw_binary);
    {
        //arma::Col<float> temp=abs(fft(dat_in.col(nx/2)));
        //temp.save("f_abs.dat",raw_binary);
    }

    //============================================================================//
    cout<<"Step 2 : FT & Choose the specific frequency band & save file"<<endl;


    printf("        (fre_min,fre_max)     =>      (%6.2fHz,%6.2fHz)\n",fre_min,fre_max);

    arma::Mat<float> dat_in_new(nz_new,nx,fill::zeros);
    arma::Mat<float> dat_out(nz_new,nx,fill::zeros);
    for(int iz=0; iz<nz; iz++)
    {
        for(int ix=0; ix<nx; ix++)
        {
            dat_in_new(iz,ix)=dat_in(iz,ix);
        }
    }
    dat_in_new.save("dat_in_new.dat",raw_binary);

    shen_choose_specific_band_2d(dat_in_new, dat_out, nz_new, nx, dt, fre_min, fre_max);

    //save every fre_band data
    string fn_dat_out="data_out_"
        + std::to_string(int(fre_min))
        + "_"+std::to_string(int(fre_max))+"Hz.dat";
    dat_out.save(fn_dat_out,raw_binary);



    //============================================================================//
    //cout<<"Step 3 : Save data"<<endl;
    //dat_out.save("dat_out.dat",raw_binary);

    //com.save("./compare.dat",raw_binary);
    //============================================================================//

    return 0;
}

