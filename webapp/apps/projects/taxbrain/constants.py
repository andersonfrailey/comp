from django.utils.safestring import mark_safe

"""
This file is used to specify constant variables such as the app's name
 and the project version.
"""
APP_NAME = "taxbrain"
APP_DESCRIPTION = APP_DESCRIPTION = mark_safe("""
<div>
    <p>
    Description here
    </p>
    <h4> Core Maintainers: </h4>
    <ul>
        <li>Anderson Frailey</li>
    </ul>
</div>
""")
TAXBRAIN_VERSION = "0.1.0"