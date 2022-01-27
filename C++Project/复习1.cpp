#include<iostream>
using namespace std;
int  main(){
	struct student {
		string name ;
		int age ;
		string sex ;
	};
	student jack ;
	cin>>jack.name >>jack.age >>jack.sex;
	cout<<jack.name<<" "<<jack.age<<" "<<jack.sex;
	return 0;
}
