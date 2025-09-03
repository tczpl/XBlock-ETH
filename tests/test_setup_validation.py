"""
Validation tests to verify the testing infrastructure is working correctly.
"""
import pytest
import sys
import os
from pathlib import Path


class TestInfrastructureSetup:
    """Test that the testing infrastructure is properly configured."""
    
    def test_python_version(self):
        """Test that Python version is supported."""
        assert sys.version_info >= (3, 8), "Python 3.8+ required"
    
    def test_pytest_import(self):
        """Test that pytest can be imported."""
        import pytest
        assert pytest.__version__
    
    def test_coverage_import(self):
        """Test that coverage tools can be imported."""
        import pytest_cov
        assert pytest_cov
    
    def test_mock_import(self):
        """Test that pytest-mock can be imported."""
        import pytest_mock
        assert pytest_mock
    
    @pytest.mark.unit
    def test_unit_marker(self):
        """Test that unit test marker works."""
        assert True
    
    @pytest.mark.integration
    def test_integration_marker(self):
        """Test that integration test marker works."""
        assert True
    
    @pytest.mark.slow
    def test_slow_marker(self):
        """Test that slow test marker works."""
        assert True


class TestProjectStructure:
    """Test that the project structure is correct."""
    
    def test_project_files_exist(self):
        """Test that main project files exist."""
        project_root = Path(__file__).parent.parent
        expected_files = [
            'README.md',
            'download.py',
            'stat_Block.py',
            'pyproject.toml'
        ]
        
        for file in expected_files:
            assert (project_root / file).exists(), f"Missing file: {file}"
    
    def test_test_directories_exist(self):
        """Test that test directories exist."""
        test_root = Path(__file__).parent
        expected_dirs = [
            'unit',
            'integration'
        ]
        
        for dir_name in expected_dirs:
            assert (test_root / dir_name).is_dir(), f"Missing directory: tests/{dir_name}"


class TestFixtures:
    """Test that shared fixtures work correctly."""
    
    def test_temp_dir_fixture(self, temp_dir):
        """Test the temp_dir fixture."""
        assert temp_dir.exists()
        assert temp_dir.is_dir()
        
        # Test that we can create files in temp dir
        test_file = temp_dir / "test.txt"
        test_file.write_text("test content")
        assert test_file.exists()
        assert test_file.read_text() == "test content"
    
    def test_sample_data_fixtures(self, sample_block_data, sample_transaction_data):
        """Test the sample data fixtures."""
        assert 'block_number' in sample_block_data
        assert 'block_hash' in sample_block_data
        assert isinstance(sample_block_data['block_number'], int)
        
        assert 'hash' in sample_transaction_data
        assert 'from_address' in sample_transaction_data
        assert isinstance(sample_transaction_data['value'], int)
    
    def test_mock_fixtures(self, mock_zip_file):
        """Test the mock fixtures."""
        assert mock_zip_file.namelist() == ['test_file.txt']
        assert mock_zip_file.read('test_file.txt') == b'test content'


def test_simple_assertion():
    """A simple test to verify basic functionality."""
    assert 1 + 1 == 2


def test_string_operations():
    """Test basic string operations."""
    test_string = "Hello, XBlock-ETH!"
    assert "XBlock-ETH" in test_string
    assert test_string.startswith("Hello")
    assert test_string.endswith("!")


@pytest.mark.parametrize("input_value,expected", [
    (1, 1),
    (2, 4),
    (3, 9),
    (4, 16),
])
def test_parametrized_square(input_value, expected):
    """Test parametrized test functionality."""
    assert input_value ** 2 == expected