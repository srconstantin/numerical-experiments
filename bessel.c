#include<stdio.h>
#include<math.h>
#include<stdlib.h>

double Bessel(double x, int n){
double const Pi = 4*atan(1);
double ans = 0;
int i;
for(i = 1; i< n+1; i++){
double y = cos((2*i-1)*Pi/(2*n));
ans = ans - 1.0/n * cos(x*y);
}
return ans;
}

int main(int argc, char** argv){
double old;
double new;
int n;
int k;

for(k = 0; k<10; k++){
for(n = 1; n<100; n++){
new = Bessel(pow(2, k), n+1);
old = Bessel(pow(2, k), n);
if (new == old){
	printf("%f \t", pow(2, k));
	printf("%f \t", new);
	printf("%d \n", n);
	break;
}
}
}
return 0;
}
