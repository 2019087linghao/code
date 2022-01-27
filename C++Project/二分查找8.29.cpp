#include<iostream>
using namespace std;


int search(int,int,int,int);
int xxx;
int aaa[10000]={0};
int len;
int  main(){ 
	cin>>len;
	cin>>xxx;
	for(int i=1;i<=len;i++){
		aaa[i]=1;
	}

	int p=search(aaa,xxx,0,8);
	if(p==-1)cout<<"no"<<endl;
	else cout<<p<<endl; 
	return 0;
	

}
int search(int arr[],int x,int left,int right){
	if(left>right){
		return -1;
	}
	else{
		int mid=(right+left)/2;
		if(arr[mid]==x)return mid;
		}else if(x>arr[mid]){
			search(arr,x,mid+1,right);
		}else if(x<arr[mid]){
			search(arr,x,left,mid-1);
		}
		
	}
	
}

