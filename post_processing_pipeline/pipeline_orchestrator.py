import logging

from post_processing_pipeline.raw_data_loader import RawDataLoader

logger = logging.getLogger(__name__)


class PipelineOrchestrator:
    """
    This is the pipeline orchestrator for python laser skreletons
    """

    def __init__(self, session_id: str = None):
        logger.info(f'Initializing Pipeline Orchestrator: {session_id}')

        if session_id is None:
            self._session_id = 'test'
        else:
            self._session_id = session_id

    @property
    def session_id(self):
        return self._session_id

    def run(self):
        logger.info('Running!')
        raw_data_loader = RawDataLoader()
        self.pupil_data = raw_data_loader.load_pupil_data(self.session_id)


if __name__ == '__main__':
    print('Starting Main Pipeline!')
    pipeline_orchestrator = PipelineOrchestrator()
    pipeline_orchestrator.run()
    print(pipeline_orchestrator.session_id)
    print('Pipeline Finished!')
