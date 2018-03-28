Program Fibo;
var I,N:integer;
    D:array [1..50] of longint;

begin
 D[1]:=1;D[2]:=1;
 Readln(N);
 for I:=3 to N do D[I]:=D[I-1]+D[I-2];
 writeln(D[N])
end.