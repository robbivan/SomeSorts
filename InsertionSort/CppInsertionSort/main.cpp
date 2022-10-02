#include <iostream>
using std::cout;
using std::endl;
int main() {
    int array[5]={12,2,5,8,3};
    int j,key=0;
    for (int i=1;i<sizeof(array)/sizeof(int);i++){
        key=array[i];
        j=i-1;
        while(key<array[j]&&(j>=0)){
            array[j+1]=array[j];
            j--;
        }
        array[j+1]=key;
        //cout<<array[i-1]<<endl;
    }

    for (int mean : array){
        cout<<mean<<endl;
    }
    return 0;
}
