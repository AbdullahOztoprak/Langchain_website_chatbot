"""
Unit tests for LLM utilities
"""

import unittest
from unittest.mock import patch, MagicMock
import os
import sys

# Add src directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.models.llm_utils import IndustrialLLMHelper, DEFAULT_SYSTEM_PROMPT

class TestIndustrialLLMHelper(unittest.TestCase):
    """Test cases for IndustrialLLMHelper class"""
    
    def setUp(self):
        """Set up test environment"""
        # Mock environment variable
        os.environ["OPENAI_API_KEY"] = "sk-test-key"
    
    @patch("src.models.llm_utils.ChatOpenAI")
    def test_initialization(self, mock_chat_openai):
        """Test initialization of the helper class"""
        # Arrange & Act
        helper = IndustrialLLMHelper(
            model_name="gpt-3.5-turbo",
            temperature=0.7
        )
        
        # Assert
        self.assertEqual(helper.model_name, "gpt-3.5-turbo")
        self.assertEqual(helper.temperature, 0.7)
        self.assertEqual(helper.system_prompt, DEFAULT_SYSTEM_PROMPT)
        self.assertEqual(helper.api_key, "sk-test-key")
        mock_chat_openai.assert_called_once_with(
            model_name="gpt-3.5-turbo",
            temperature=0.7,
            openai_api_key="sk-test-key"
        )
    
    @patch("src.models.llm_utils.ChatOpenAI")
    def test_get_chat_response(self, mock_chat_openai):
        """Test getting a chat response"""
        # Arrange
        mock_instance = MagicMock()
        mock_generation = MagicMock()
        mock_generation.generations = [[MagicMock(text="Test response")]]
        mock_instance.generate.return_value = mock_generation
        mock_chat_openai.return_value = mock_instance
        
        helper = IndustrialLLMHelper()
        messages = [
            {"role": "user", "content": "Hello"}
        ]
        
        # Act
        response = helper.get_chat_response(messages)
        
        # Assert
        self.assertEqual(response, "Test response")
        mock_instance.generate.assert_called_once()
    
    @patch("src.models.llm_utils.ChatOpenAI")
    def test_change_model(self, mock_chat_openai):
        """Test changing the model"""
        # Arrange
        helper = IndustrialLLMHelper(model_name="gpt-3.5-turbo")
        mock_chat_openai.reset_mock()
        
        # Act
        helper.change_model("gpt-4")
        
        # Assert
        self.assertEqual(helper.model_name, "gpt-4")
        mock_chat_openai.assert_called_once_with(
            model_name="gpt-4",
            temperature=helper.temperature,
            openai_api_key=helper.api_key
        )
    
    @patch("src.models.llm_utils.ChatOpenAI")
    def test_change_temperature(self, mock_chat_openai):
        """Test changing the temperature"""
        # Arrange
        helper = IndustrialLLMHelper(temperature=0.7)
        mock_chat_openai.reset_mock()
        
        # Act
        helper.change_temperature(0.5)
        
        # Assert
        self.assertEqual(helper.temperature, 0.5)
        mock_chat_openai.assert_called_once_with(
            model_name=helper.model_name,
            temperature=0.5,
            openai_api_key=helper.api_key
        )
    
    @patch("src.models.llm_utils.ChatOpenAI")
    def test_invalid_temperature(self, mock_chat_openai):
        """Test setting invalid temperature"""
        # Arrange
        helper = IndustrialLLMHelper()
        
        # Act & Assert
        with self.assertRaises(ValueError):
            helper.change_temperature(1.5)
    
    def test_get_industrial_examples(self):
        """Test getting industrial examples"""
        # Arrange
        helper = IndustrialLLMHelper()
        
        # Act
        examples = helper.get_industrial_examples()
        
        # Assert
        self.assertIsInstance(examples, list)
        self.assertTrue(len(examples) > 0)
        for example in examples:
            self.assertIn("question", example)
            self.assertIn("topic", example)

if __name__ == "__main__":
    unittest.main()
