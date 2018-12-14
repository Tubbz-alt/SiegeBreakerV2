/*
Author : SiegeBreaker Devs.
*/
#include <stdio.h>

typedef struct TCP_ID {
    int port;
} TCP_ID;


typedef struct db_mgr {

    int db_size;
    struct TCP_ID tcp_id[30];
} db_mgr;

