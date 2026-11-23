metadata(description="Fixture package.", version="1.2.3")

require("fixture-dependency")
module("fixture_demo.py", opt=3)
package("fixture_helpers", files=("__init__.py", "codec.py"))
