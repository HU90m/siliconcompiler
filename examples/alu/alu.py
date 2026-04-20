from pathlib import Path

from siliconcompiler import Design, Project
from siliconcompiler.flows.lintflow import LintFlow

DATA_ROOT: tuple[str, str] = ("alu", str(Path(__file__).parents[0]))


class TypesPkg(Design):
    def __init__(self) -> None:
        super().__init__("types_pkg")
        self.set_dataroot(*DATA_ROOT)
        self.add_file("types_pkg.sv", dataroot=DATA_ROOT[0], fileset="rtl")

class AluPkg(Design):
    def __init__(self):
        super().__init__("alu_pkg")
        self.set_dataroot(*DATA_ROOT)

        with self.active_dataroot(DATA_ROOT[0]), self.active_fileset("rtl"):
            self.add_idir("includes")
            self.add_file("alu_pkg.sv")
            self.add_depfileset(TypesPkg())

class Alu(Design):
    def __init__(self):
        super().__init__("alu")
        self.set_dataroot(*DATA_ROOT)

        with self.active_dataroot(DATA_ROOT[0]), self.active_fileset("rtl"):
            self.add_depfileset(AluPkg())
            self.add_file("alu.sv")
            self.set_topmodule("alu")


if __name__ == "__main__":
    project = Project()
    project.set_design(Alu())
    # If you change the tool to 'verilator' the lint should fail,
    # due to the file order.
    project.set_flow(LintFlow(tool="slang"))
    project.add_fileset("rtl")
    project.check_manifest()
    project.run()
