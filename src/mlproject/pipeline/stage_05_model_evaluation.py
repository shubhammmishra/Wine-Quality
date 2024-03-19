from mlproject.config.configuration import ConfigurationManager
from mlproject.components.model_evaluation import ModelEvaluation
from mlproject import logger

STAGE_NAME = "mode evaluation stage"

class ModelEvaluationTrainingPipeline:
    def init(self):
        pass

    
    def main(self):
    
        
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation_config = ModelEvaluation(config = model_evaluation_config)
            model_evaluation_config.save_results()

if __name__ == '__main()__':
    try:
        logger.info(f" stage {STAGE_NAME} started")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f"stage {STAGE_NAME} completed")
    except Exception as e:
        logger.exception(e)
        raise e

    