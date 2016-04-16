.z.zd:16 1 0i;
args:.Q.opt .z.x;
src:`$first args`source;
upd:insert;
hsrc:hopen src
startup:hsrc({ .u.sub[]; (tplog;{(x;0#value x)}each tables `.) };0);
{ .[x;();:;y] }./:last startup;
rttables:tables `.;
-11!first startup;
endofday:{[donedate]
    {[dt].Q.dpft[`:./data/;dt;`sym]each rttables}[donedate];
    {delete from x}each rttables;
  };
