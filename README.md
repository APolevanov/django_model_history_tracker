# Django Model History Tracker

Django Model History Tracker is a utility that tracks changes to model instances and saves the history of updates. This can be helpful for auditing purposes or for generating reports about changes over time.

## Features

- Track creation, update, and deletion of model instances
- Store historical data in a separate `History` model
- Easy integration with existing Django models using a mixin

## Installation

1. Install the package using pip:

pip install django-model-history-tracker

2. Add `'django_model_history_tracker'` to your `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'django_model_history_tracker',
    ...
]

python manage.py migrate


 ## Usage

To use Django Model History Tracker, simply inherit the HistoryTrackerMixin in any model you want to track:

from django.db import models
from django_model_history_tracker.mixins import HistoryTrackerMixin

class ExampleModel(HistoryTrackerMixin, models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()

That's it! Your model will now automatically track changes and store them in the History model.


Accessing History

You can access the history of a tracked model instance using the generic relation:

history = example_model_instance.history_set.all()

Each history entry will have the following fields:

    action: The action that occurred ('create', 'update', or 'delete')
    timestamp: The timestamp of when the action occurred
    changes: A JSON field containing the changes made to the instance


Contributing

Contributions are welcome! Please feel free to submit issues or pull requests on the GitHub repository.


License

This project is licensed under the MIT License. See the LICENSE file for details.