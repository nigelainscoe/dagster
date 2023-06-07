from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, Any, Mapping, Optional, Sequence

from dagster import get_dagster_logger
from dagster._annotations import deprecated

if TYPE_CHECKING:
    import logging

    from .types import DbtOutput


class DbtClient:
    """Base class for a client allowing users to interface with dbt."""

    def __init__(
        self,
        logger: Optional[logging.Logger] = None,
    ):
        """Constructor.

        Args:
            logger (Optional[Any]): A property for injecting a logger dependency.
                Default is ``None``.
        """
        self._logger = logger or get_dagster_logger()

    def _format_params(
        self, flags: Mapping[str, Any], replace_underscores: bool = False
    ) -> Mapping[str, Any]:
        """Reformats arguments that are easier to express as a list into the format that dbt expects,
        and deletes and keys with no value.
        """
        # remove any keys with a value of None
        if replace_underscores:
            flags = {k.replace("_", "-"): v for k, v in flags.items() if v is not None}
        else:
            flags = {k: v for k, v in flags.items() if v is not None}

        for param in ["select", "exclude", "models"]:
            if param in flags:
                if isinstance(flags[param], list):
                    # if it's a list, format as space-separated
                    flags[param] = " ".join(set(flags[param]))

        return flags

    @property
    def logger(self) -> logging.Logger:
        """logging.Logger: A property for injecting a logger dependency."""
        return self._logger

    @abstractmethod
    def compile(
        self,
        models: Optional[Sequence[str]] = None,
        exclude: Optional[Sequence[str]] = None,
        **kwargs,
    ) -> DbtOutput:
        """Run the ``compile`` command on a dbt project. kwargs are passed in as additional parameters.

        Args:
            models (List[str], optional): the models to include in compilation.
            exclude (List[str]), optional): the models to exclude from compilation.

        Returns:
            DbtOutput: object containing parsed output from dbt
        """

    @abstractmethod
    def run(
        self,
        models: Optional[Sequence[str]] = None,
        exclude: Optional[Sequence[str]] = None,
        **kwargs,
    ) -> DbtOutput:
        """Run the ``run`` command on a dbt project. kwargs are passed in as additional parameters.

        Args:
            models (List[str], optional): the models to include in the run.
            exclude (List[str]), optional): the models to exclude from the run.

        Returns:
            DbtOutput: object containing parsed output from dbt
        """

    @abstractmethod
    def snapshot(
        self,
        select: Optional[Sequence[str]] = None,
        exclude: Optional[Sequence[str]] = None,
        **kwargs,
    ) -> DbtOutput:
        """Run the ``snapshot`` command on a dbt project. kwargs are passed in as additional parameters.

        Args:
            select (List[str], optional): the snapshots to include in the run.
            exclude (List[str], optional): the snapshots to exclude from the run.

        Returns:
            DbtOutput: object containing parsed output from dbt
        """

    @abstractmethod
    def test(
        self,
        models: Optional[Sequence[str]] = None,
        exclude: Optional[Sequence[str]] = None,
        data: bool = True,
        schema: bool = True,
        **kwargs,
    ) -> DbtOutput:
        """Run the ``test`` command on a dbt project. kwargs are passed in as additional parameters.

        Args:
            models (List[str], optional): the models to include in testing.
            exclude (List[str], optional): the models to exclude from testing.
            data (bool, optional): If ``True`` (default), then run data tests.
            schema (bool, optional): If ``True`` (default), then run schema tests.

        Returns:
            DbtOutput: object containing parsed output from dbt
        """

    @abstractmethod
    def seed(
        self,
        show: bool = False,
        select: Optional[Sequence[str]] = None,
        exclude: Optional[Sequence[str]] = None,
        **kwargs,
    ) -> DbtOutput:
        """Run the ``seed`` command on a dbt project. kwargs are passed in as additional parameters.

        Args:
            show (bool, optional): If ``True``, then show a sample of the seeded data in the
                response. Defaults to ``False``.
            select (List[str], optional): the snapshots to include in the run.
            exclude (List[str], optional): the snapshots to exclude from the run.


        Returns:
            DbtOutput: object containing parsed output from dbt
        """

    @abstractmethod
    def ls(
        self,
        select: Optional[Sequence[str]] = None,
        models: Optional[Sequence[str]] = None,
        exclude: Optional[Sequence[str]] = None,
        **kwargs,
    ) -> DbtOutput:
        """Run the ``ls`` command on a dbt project. kwargs are passed in as additional parameters.

        Args:
            select (List[str], optional): the resources to include in the output.
            models (List[str], optional): the models to include in the output.
            exclude (List[str], optional): the resources to exclude from the output.


        Returns:
            DbtOutput: object containing parsed output from dbt
        """

    @abstractmethod
    def build(self, select: Optional[Sequence[str]] = None, **kwargs) -> DbtOutput:
        """Run the ``build`` command on a dbt project. kwargs are passed in as additional parameters.

        Args:
            select (List[str], optional): the models/resources to include in the run.

        Returns:
            DbtOutput: object containing parsed output from dbt
        """
        raise NotImplementedError()

    @abstractmethod
    def generate_docs(self, compile_project: bool = False, **kwargs) -> DbtOutput:
        """Run the ``docs generate`` command on a dbt project. kwargs are passed in as additional parameters.

        Args:
            compile_project (bool, optional): If true, compile the project before generating a catalog.

        Returns:
            DbtOutput: object containing parsed output from dbt
        """

    @abstractmethod
    def run_operation(
        self, macro: str, args: Optional[Mapping[str, Any]] = None, **kwargs
    ) -> DbtOutput:
        """Run the ``run-operation`` command on a dbt project. kwargs are passed in as additional parameters.

        Args:
            macro (str): the dbt macro to invoke.
            args (Dict[str, Any], optional): the keyword arguments to be supplied to the macro.

        Returns:
            DbtOutput: object containing parsed output from dbt
        """

    @abstractmethod
    def get_run_results_json(self, **kwargs) -> Optional[Mapping[str, Any]]:
        """Get a parsed version of the run_results.json file for the relevant dbt project.

        Returns:
            Dict[str, Any]: dictionary containing the parsed contents of the run_results json file
                for this dbt project.
        """

    @abstractmethod
    def get_manifest_json(self, **kwargs) -> Optional[Mapping[str, Any]]:
        """Get a parsed version of the manifest.json file for the relevant dbt project.

        Returns:
            Dict[str, Any]: dictionary containing the parsed contents of the manifest json file
                for this dbt project.
        """


@deprecated
class DbtResource(DbtClient):
    pass
