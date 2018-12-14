
/*
Author : SiegeBreaker Devs.
*/
#include "custom_base64.h"
#include "custom_parser.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <stdlib.h>

#define PORT 443
#define maxsize 65536


#define self_ip "192.168.2.5"

#define URL_VAL "https://10.1.5.2/test_file.txt"


void *thread_handler_function(void *_void_thread_mgr) {

    thread_mgr *thMgr = (thread_mgr *) _void_thread_mgr;


    int db_id = gen_entry_and_add(thMgr->weak_db_ref, (thMgr->last_pkt)->ip, (thMgr->last_pkt)->port);

    char system_str[2048] = {" "};

    int len_base64;
    char *baseOP = base64((thMgr->last_pkt)->msg, 32, &len_base64);

    printf("Running Single Conn Queue\n");
    int inserted_char = sprintf(system_str, "./single_conn_queue.o \"%lu::%lu::%d::%d::%d::%d::%s::%d::%d::",
                                (thMgr->last_pkt)->reply_ack,
                                (thMgr->last_pkt)->reply_seq,
                                (thMgr->last_pkt)->urg_ptr,
                                (thMgr->last_pkt)->window,
                                (thMgr->last_pkt)->port,
                                (thMgr->last_pkt)->length,
                                (thMgr->last_pkt)->ip,
                                0,
                                len_base64
    );


    strncpy(&system_str[inserted_char], baseOP, len_base64);
    inserted_char += len_base64;


    strncpy(&system_str[inserted_char], "::", 2);

    inserted_char += 2;


    int size_msg = strlen(&((thMgr->last_pkt)->msg[32]));


    strncpy(&system_str[inserted_char], &((thMgr->last_pkt)->msg[32]), size_msg);

    strncpy(&system_str[inserted_char + size_msg], "::\"", 3);


    strncpy(&system_str[inserted_char + size_msg + 3], "  ;\0", 4);


    int end = inserted_char + size_msg + 3 + 4;

    printf("CMD : ");

    int i;
    for (i = 0; i < end; ++i) {

        if (system_str[i] == '&')
            break;

        if (system_str[i] == '\0' || system_str[i] == '\n') {
            printf("culprit at index %d", i);
        }

    }
    printf("\n");


    fflush(stdout);

    int delay = 10000;

    while (delay--) {}

    system(system_str);


    return NULL;
}


char *concat(const char *s1, const char *s2) {
    char *result = malloc(strlen(s1) + strlen(s2) + 1);//+1 for the null-terminator

    strcpy(result, s1);
    strcat(result, s2);
    return result;
}


int main() {

    int server_fd, new_socket, valread;


    char buffer[maxsize] = {0};




    /************************libpcap initialization*******************************/
    char dev[] = {"eth0"};
    char errbuf[PCAP_ERRBUF_SIZE];
    pcap_t *descr;
    u_char *packet;
    struct pcap_pkthdr hdr;     /* pcap.h */
    struct ether_header *eptr;  /* net/ethernet.h */
    struct bpf_program filter;


    char filter_exp[1024] = {""};

    int bytes_written = sprintf(filter_exp,
                                "dst port %d and dst host 192.168.2.5 and not src host 192.168.2.4 and not icmp and greater 150",
                                443);

    printf("filter_exp %s\n", filter_exp);

//    char filter_exp[] = "dst port 443";


    bpf_u_int32 ipaddr;

    u_char *ptr; /* printing out hardware header info */

    printf("DEV: %s\n", dev);

    /* open the device for sniffing.

       pcap_t *pcap_open_live(char *device,int snaplen, int prmisc,int to_ms,
       char *ebuf)

       snaplen - maximum size of packets to capture in bytes
       promisc - set card in promiscuous mode?
       to_ms   - time to wait for packets in miliseconds before read
       times out
       errbuf  - if something happens, place error string here

       Note if you change "prmisc" param to anything other than zero, you will
       get all packets your device sees, whether they are intendeed for you or
       not!! Be sure you know the rules of the network you are running on
       before you set your card in promiscuous mode!!     */


    descr = pcap_open_live(dev, BUFSIZ, 0, 1, errbuf);

    if (descr == NULL) {
        printf("pcap_open_live(): %s\n", errbuf);
        exit(1);
    }

    if (pcap_compile(descr, &filter, filter_exp, 0, ipaddr) == -1) {
        printf("Bad filter - %s\n", pcap_geterr(descr));
        return 2;
    }
    if (pcap_setfilter(descr, &filter) == -1) {
        printf("Error setting filter - %s\n", pcap_geterr(descr));
        return 2;
    }
    /*****************************libpcap init end********************************/




    printf("-> Starting Reading from SOCK_RAW Socket %d\n", PORT);

    pthread_t inc_x_thread[10];

    int g_thread_counter = 0;
    db_mgr *g_db_structure = init_db();

//	gen_entry_and_add( g_db_structure , "10.1.5.2", 443);


    // check_main(g_db_structure);
    // exit(0);


    while (1) {

        // len = recvfrom(sock, recvbuf, sizeof(recvbuf), 0 ,(struct sockaddr_in *)&pFrom , &iFromSize);

        //  printf(" %d %s\n", len , recvbuf );


        KeyObj *iKey = (KeyObj *) malloc(sizeof(KeyObj));
        iKey->key_value = (char *) malloc(sizeof(char) * 32);
        iKey->isRSA_priv = 1;


        printf("Listening....\n");

        Sniff_response *packtObj = sniff_center(descr, self_ip, NULL, 1, iKey, g_db_structure);


        if (packtObj == NULL) continue;

        strncpy(iKey->key_value, packtObj->msg, 32);


        if (!packtObj->msg || packtObj->msg[32] != 'h') {
            printf("Invalid url inside center  \n");
            fflush(stdout);

            continue;
        }

        //printf(" KEY_VAL : %s \n",iKey->key_value );

        iKey->isRSA_priv = 0;


        printf("-> printing packet\n");
        printf("-> packet ip : %s\n", packtObj->ip);
        printf("-> port : %d\n", packtObj->port);

        printf("-> D  port : %d\n", packtObj->dport);

        printf("-> seq : %lu\n", packtObj->reply_seq);
        printf("-> ack : %lu\n", packtObj->reply_ack);

        if (validate_new_connection(g_db_structure, packtObj)) {


            //Thread args setup

            thread_mgr *thMgr = (thread_mgr *) calloc(sizeof(thread_mgr), 1);
            thMgr->last_pkt = NULL;
            thMgr->last_pkt = (packtObj);
            thMgr->socket_id = 0;
            thMgr->weak_db_ref = g_db_structure;

            if (pthread_create(&(inc_x_thread[g_thread_counter]), NULL,
                               thread_handler_function, &(*thMgr))) {
                fprintf(stderr, "Error creating thread\n");
                return 1;
            }

        }

        // if(pthread_join(inc_x_thread, NULL)) 
        // {
        //     fprintf(stderr, "Error joining thread\n");
        //     return 2;
        // }
    }





// typedef struct packtObj_RESPONSE {
//   char *msg;
//   unsigned long reply_ack;
//   unsigned long reply_seq;
//   int urg_ptr;
//   int window;
//   int port;
//   int length;
//   char *ip;
// } packtObj_response;


}

