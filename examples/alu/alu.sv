module alu
    import types_pkg::data_t;
    import alu_pkg::*;
(
    input  opcode_e     opcode_i,
    input  data_t       a_i,
    input  data_t       b_i,
    output alu_result_t result_o
);
    data_t value;
    logic carry;

    always_comb begin
      carry = 0;
      unique case (opcode_i)
        OP_ADD: {carry, value} = a_i + b_i;
        OP_SUB: value = a_i - b_i;
        OP_AND: value = a_i & b_i;
        OP_OR:  value = a_i | b_i;
      endcase
    end

    assign result_o = '{
      value: value,
      carry: carry,
      zero: (value == '0)
    };
endmodule : alu
