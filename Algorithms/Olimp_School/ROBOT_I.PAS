Program robot;
Var Way1,Way2:array [-16..16,-16..16] of longint;
    X,Y,K,i,j,z:shortint;s:longint;
begin

 readln(K,X,Y);
 for i:=-16 to 16 do
  for j:=-16 to 16 do
    Way1[i,j]:=0;
 Way1[0,0]:=1;
 for z:=1 to k do
  begin
   Way2:=Way1;
   for i:=-16 to 16 do
    for j:=-16 to 16 do
     begin
      s:=0;
      if i<>-16 then s:=s+Way2[i-1,j];
      if i<>16 then s:=s+Way2[i+1,j];
      if j<>-16 then s:=s+Way2[i,j-1];
      if j<>16 then s:=s+Way2[i,j+1];
      Way1[i,j]:=s;
     end;
  end;
 writeln(way1[x,y]);
end.