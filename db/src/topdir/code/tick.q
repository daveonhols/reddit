/ hclose loghandle
\l code/reddit.q
startTime:.z.z;
tplog:`$":./tplog/",string `date$startTime;
prevTime:`time$startTime;
if[()~key tplog;.[tplog;();:;()]];
loghandle:hopen tplog;

subscriber:0N;

.u.upd:{[tbl;data]
    if[not 19h=abs type first data;data:(enlist enlist .z.t),enlist each data];
    if[prevTime>currTime:first raze first data;
        endofday[]];
    `prevTime set currTime;
    msg:(`upd;tbl;data);
    loghandle @ enlist  msg;
    .u.pub[tbl;data];
  };

/ endofday[]
endofday:{
    hclose loghandle;
    nextDay:1+prevDay:`date$startTime;
    `tplog set `$":./tplog/",string nextDay;
    `startTime set `datetime$nextDay;
    .[tplog;();:;()];
    `loghandle set hopen tplog;
    (neg subscriber) @ (`endofday;prevDay)
  };

.u.pub:{[tbl;data]
    if[null subscriber;:()];
    (neg subscriber) @ (`upd;tbl;data)
  };

.u.sub:{[]
    `subscriber set .z.w;
  };

.z.pc:{[handle]
    show "gone away: ",-3!handle;
    if[handle=subscriber;`subscriber set 0N];
  };

