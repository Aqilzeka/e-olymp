'''
def function(x,y):
    if B[x][y] == -1:
        if function(x-1,y) > function(x,y-1):
            B[x][y] = max(function(x-1,y) + A[x][y], B[x][y] = function(x,y-1) + A[x][y]
    return B[x][y]


n = int(input())

 for i:=1 to N do
  begin
   for j:=1 to N-1 do
    read(A[i,j]);
   readln(A[i,N])
  end;
 for i:=1 to N do
  for j:=1 to N do
   B[i,j]:=-1;
 for i:=0 to N do
  begin
   B[i,0]:=0;
   B[0,j]:=0
  end;
 writeln(F(N,N));
end.
'''