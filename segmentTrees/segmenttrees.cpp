#include<bits/stdc++.h>
using namespace std;

void buildTree(vector<int>&arr,vector<int>&tree,int start,int end,int Treenode){
      if(start==end){
            tree[Treenode]=arr[start];
            return;
      }
      int mid=(start+end)/2;
      buildTree(arr,tree,start,mid,2*Treenode);
      buildTree(arr,tree,mid+1,end,2*Treenode+1);
      tree[Treenode]=tree[2*Treenode]+tree[2*Treenode+1];

}
void update(vector<int>&arr,vector<int>&tree,int start,int end,int Treenode,int index,int value){
      
      if(start==end){
            arr[index]=value;
            tree[Treenode]=value;
            return;
      }
      int mid=(start+end)/2;
      //right
      if(index>mid){
            update(arr,tree,mid+1,end,2*Treenode+1,index,value);
      }
      //left
      else{
            update(arr,tree,start,mid,2*Treenode,index,value);

      }
     tree[Treenode]=tree[2*Treenode]+tree[2*Treenode+1];
}

int query(vector<int>&tree,int start,int end,int left,int right,int Treenode){
      //complete otside range
       if(start>right || end<left){
            return 0;
       }
      //complete inside range
      if(start>=left && end<=right){
            return tree[Treenode];
      }
      //partially out or partially in
      int mid=start+end/2;
      //right call
      int ans1=query(tree,start,mid,left,right,2*Treenode);
      int ans2=query(tree,mid+1,end,left,right,2*Treenode+1);;
      return ans1+ans2;
}
int main(){
      //ideally we have to take size of tree array is 4n
      //there is a derivation behind this
      vector<int>arr={1,2,3,4,5};
      vector<int>tree(20);
      buildTree(arr,tree,0,4,1);
      update(arr,tree,0,4,1,2,10);
      int ans=query(tree,0,4,2,4,1);
      cout<<ans;

}