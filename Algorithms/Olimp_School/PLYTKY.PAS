Program Matrix;

Type SuperInt=array [1..50] of shortint;
     SimpMat=array [1..3] of SuperInt;

Procedure Add(a,b:SuperInt;var c:SuperInt);
var r,i,m:integer;
begin
 m:=0;
 for i:=1 to 50 do
  begin
   r:=a[i]+b[i]+m;
   c[i]:=r mod 10;
   m:=r div 10;
  end;
end;

Procedure Print(a:SuperInt);
var f:boolean;i:integer;
begin
 f:=True;i:=50;
 while i>0 do
  begin
   if a[i]>0 then f:=False;
   if not f then write(a[i]);
   i:=i-1;
  end;
 if f then writeln('0') else writeln;
end;



Function Check(i,j:shortint;s:integer):integer;
var r,k:integer;
begin
 if i>j then begin k:=j;j:=i;i:=k end;
 if i=2 then j:=j+2;
 if i=3 then j:=j+3;
 r:=1;
 for k:=1 to j-1 do
  r:=r*2;
 Check:=s or r;
end;

Var na,a:array [0..63] of SimpMat;
    rs,i,n,k,l,NewS,count:integer;
    s1,s2,s3:string;
    z:SuperInt;

begin
 Readln(n);
 Readln(s1);Readln(s2);Readln(s3);
 FillChar(a,sizeof(a),0);a[0][1][1]:=1;a[0][2][1]:=1;a[0][3][1]:=1;
 FOR COUNT:=2 to N do
 BEGIN
 FillChar(na,sizeof(a),0);
 for i:=0 to 63 do
  begin
   for l:=1 to 3 do
    for k:=1 to 3 do
     begin
       NewS:=Check(l,k,i);
       Add(Na[News][k],A[i][l],Na[NewS][k]);
     end;
  end;
  a:=na;
 END;
 rs:=0;
 if s1[1]='Y' then rs:=rs+1;
 if s1[2]='Y' then rs:=rs+2;
 if s1[3]='Y' then rs:=rs+4;
 if s2[2]='Y' then rs:=rs+8;
 if s2[3]='Y' then rs:=rs+16;
 if s3[3]='Y' then rs:=rs+32;
 Add(Na[rs][1],Na[rs][2],z);
 Add(z,Na[rs][3],z);
 Print(z);
 Close(input);
 close(output);
end.