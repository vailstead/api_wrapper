# api_wrapper

# git commit hooks
```
pip install -r docs/requirements.txt
pre-commit install
```

# pylint
Pylint is used in pre-commit hooks. It can also be ran manually.  
Manually via pylint: ```pylint *```  
Manually via pre-commit (check only staged files): ``` pre-commit run --all-files```  
Automated via git commit (checks only staged files)

Note: configure pylint behavior via .pylintrc file

# pytest
Tests lie in test/ directory. Run ```pytest``` from project run to run tests.
