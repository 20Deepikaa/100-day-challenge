#include <stdio.h>

int main(void) {
	// your code goes here
		int n,a,b,c,i;
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
	scanf("%d %d %d",&a,&b,&c);
	if(a==1)
	{
	printf("%d\n",(b*c));
	}
	else if(a>1&&b==1)
	{
	    printf("%d\n",(a*c));
	}
	else
	{
	    printf("%d\n",(a*b*c));
	}
	}
	return 0;
}
