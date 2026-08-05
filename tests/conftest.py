"""
Shared pytest fixtures for the XBlock-ETH project.
"""
import os
import tempfile
import shutil
import zipfile
from pathlib import Path
from unittest.mock import Mock, patch
import pytest


@pytest.fixture
def temp_dir():
    """Create a temporary directory for test files."""
    temp_path = tempfile.mkdtemp()
    yield Path(temp_path)
    shutil.rmtree(temp_path, ignore_errors=True)


@pytest.fixture
def mock_zip_file():
    """Create a mock zipfile for testing."""
    mock_zip = Mock(spec=zipfile.ZipFile)
    mock_zip.namelist.return_value = ['test_file.txt']
    mock_zip.read.return_value = b'test content'
    return mock_zip


@pytest.fixture
def sample_block_data():
    """Sample block data for testing."""
    return {
        'block_number': 123456,
        'block_hash': '0x123abc...',
        'timestamp': 1234567890,
        'transaction_count': 10
    }


@pytest.fixture
def sample_transaction_data():
    """Sample transaction data for testing."""
    return {
        'hash': '0xabc123...',
        'block_number': 123456,
        'from_address': '0x111...',
        'to_address': '0x222...',
        'value': 1000000000000000000,  # 1 ETH in wei
        'gas': 21000,
        'gas_price': 20000000000
    }


@pytest.fixture
def mock_requests_get():
    """Mock requests.get for testing downloads."""
    with patch('requests.get') as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.headers = {'content-length': '1024'}
        mock_response.iter_content.return_value = [b'test data chunk']
        mock_get.return_value.__enter__.return_value = mock_response
        yield mock_get


@pytest.fixture
def mock_file_operations():
    """Mock file operations for testing."""
    with patch('builtins.open'), \
         patch('os.path.exists'), \
         patch('os.remove'), \
         patch('os.rename'):
        yield


@pytest.fixture
def sample_zip_files():
    """Create sample zip files for testing."""
    return [
        '0to999999_Block.zip',
        '1000000to1999999_Block.zip',
        'stat_Block.py'
    ]


@pytest.fixture
def mock_time_sleep():
    """Mock time.sleep to speed up tests."""
    with patch('time.sleep') as mock_sleep:
        yield mock_sleep


@pytest.fixture
def clean_environment():
    """Ensure clean test environment by removing test files."""
    test_files = [
        'test_file.temp',
        'test_file.zip',
        'test_output.txt'
    ]
    
    # Clean before test
    for file in test_files:
        if os.path.exists(file):
            os.remove(file)
    
    yield
    
    # Clean after test
    for file in test_files:
        if os.path.exists(file):
            os.remove(file)


@pytest.fixture(autouse=True)
def no_network_calls():
    """Prevent actual network calls during tests."""
    with patch('requests.get') as mock_get:
        mock_get.side_effect = Exception("Network calls not allowed in tests")
        yield mock_get


@pytest.fixture
def mock_user_input():
    """Mock user input for interactive tests."""
    def _mock_input(return_value="1"):
        with patch('builtins.input', return_value=return_value) as mock:
            yield mock
    return _mock_input