Program Ball;
var I,N:integer;
    D:array [1..30] of longint;

begin
 D[1]:=1;D[2]:=2;D[3]:=4;
 Readln(N);
 for I:=4 to N do D[I]:=D[I-1]+D[I-2]+D[I-3];
 writeln(D[N])
end.
