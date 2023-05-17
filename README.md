# todo_by

Runtime lifetimes for comments. Inspired by
[parker-codes/todo_by](https://github.com/parker-codes/todo_by).

To use the library, install it using `pip`:


```bash
pip install todo_by
```

Then import and use it like so:

```python
from todo_by import todo_by

@todo_by("2023-06-01")
def my_function():
    # TODO: Implement this function by June 1st, 2023
```
If the current date is after June 1st, 2023, the `todo_by` decorator will
generate a `RuntimeError` with the message `"TODO by Jun 1, 2023 has passed"`.  
If the current date is on or before June 1st, 2023, the code will run normally.

You can also add specific TODO comments:

```python
@todo_by("2023-06-01", "Clean up implementation")
```

## License:

```
Copyright 2023 Martin Simon

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

## Buy me a coffee?

If you feel like buying me a coffee (or a beer?), donations are welcome:

```
BTC : bc1qq04jnuqqavpccfptmddqjkg7cuspy3new4sxq9
DOGE: DRBkryyau5CMxpBzVmrBAjK6dVdMZSBsuS
ETH : 0x2238A11856428b72E80D70Be8666729497059d95
LTC : MQwXsBrArLRHQzwQZAjJPNrxGS1uNDDKX6
```
