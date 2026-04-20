`include "alu_defs.svh"

package alu_pkg;
    import types_pkg::data_t;

    typedef enum logic [1:0] {
        OP_ADD = `OP_ADD,
        OP_SUB = `OP_SUB,
        OP_AND = `OP_AND,
        OP_OR  = `OP_OR
    } opcode_e;

    typedef struct packed {
        data_t  value;
        logic   carry;
        logic   zero;
    } alu_result_t;
endpackage
