from __future__ import annotations

from dagster_managed_elements import ManagedElementDiff

from dagster_managed_elements_tests.example_reconciler import MyManagedElementReconciler

my_reconciler = MyManagedElementReconciler(ManagedElementDiff())
