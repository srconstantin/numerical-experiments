#include<stdio.h>
#include<math.h>
#include<stdlib.h>


void HermiteUpdate(double* poly, double* prevpoly, int k, double* newpoly){
int i;
newpoly[0] = -2*(k-1)*prevpoly[0];
for(i= 0; i<k+1; i++){
newpoly[i] = 2*poly[i-1] - 2*(k-1)*prevpoly[i];
}

}

void NewtonRoot(double guess, double* coeffs, int n, double root){
int i;
int j;
double value = guess;
double derivative[1000];
double f = 0;
double g=0;
for(i = 0; i<n; i++){
derivative[i] = (i+1)*coeffs[i+1];
}
for(i = 0; i<10; i++){ 
for(j = 0; j<n+1; j++){
	f = f + coeffs[j]*pow(value, j);
}

for(j = 0; j<n; j++){
	g= g+ derivative[j]*pow(value, j);
}
value = value - f/g;
f = 0;
g = 0;
} 
root = value;
 printf(" %f \n", root); 
}


int main(){
int i;
int j;
double prevpoly[1000];
prevpoly[0] = 1;
for(i = 1; i<1000; i++){
prevpoly[i] = 0;
}
/*printf(" %d \n ", prevpoly[0]); */
double poly[1000];
poly[0] = 0;
poly[1] = 2;
for(i = 2; i<1000; i++){
poly[i] = 0;
}
/*printf(" %d \t", poly[0]);
printf(" %d \n", poly[1]); */

int k = 37;
double newpoly[1000];
for(i =0; i<1000; i++){
newpoly[i] = 0;
}

for(i = 2; i<k+1; i++){
HermiteUpdate(poly, prevpoly, i, newpoly);
/* for(j = 0; j<i+1; j++){
printf(" %d \t", newpoly[j]);
} 
printf(" \n ");*/
for(j = 0; j < i+1; j++){
prevpoly[j] = poly[j];
}
for(j = 0; j<i+1; j++){
poly[j] = newpoly[j];
}
}
/* for(j = 0; j<i+1; j++){
printf(" %f \t", newpoly[j]);
} 
printf(" \n "); */

/* divide (-9, 9) into small increments */
/*evaluate polynomial at each point and note if there's a difference of sign between successive points. */
int sgn[180];
double value = 0;
double t;

for(t = -9; t <= 9; t=t+0.1){
for(j = 0; j <= 37; j++){
value = value + newpoly[j]* pow(t, j);
}
i = (int) 10*(t+9);
if (value > 0){
	sgn[i] = 1;
	}
if (value < 0){
	sgn[i] = -1;
	}


value = 0;
}

/*for(i = 0; i<180; i++){
printf(" %d \t", sgn[i]);
}*/



double root;
for(i = 0; i<180; i++){
t = (double) (i+1)/10 - 9;
if (sgn[i] != sgn[i+1]){
printf(" %f \t", t);
NewtonRoot(t, newpoly, 37, root);
}
} 
return 0;
}
