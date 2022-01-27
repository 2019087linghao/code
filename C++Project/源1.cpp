#include<iostream>
using namespace std;
struct xxx{
	float x;
	bool xx;
	float Area(){
		
		return x*x*3.14;
	}
};
int main(){
	xxx abc;
	float i;
	cin>>i;
	abc.x=i;
	cout<<abc.Area()<<endl;
	cout<<abc.x<<endl;
	return 0;
}