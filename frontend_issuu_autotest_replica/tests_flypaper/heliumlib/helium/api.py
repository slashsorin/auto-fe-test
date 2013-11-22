"""
Helium Copyright (c) 2012-2013 BugFree Software. All Rights Reserved.

The helium.api module contains the implementation and API of Helium. It is
a simple Python API that makes specifying web automation cases as simple as
describing them to someone looking over their shoulder at a screen.

The public functions and classes of Helium are listed below. If you wish to use
Helium functions in your Python scripts you can import them from the
``helium.api`` module::

	from helium.api import *
"""
from __future__ import absolute_import
from collections import namedtuple
from copy import copy
from decorator import decorator
from helium.api_impl.application_context import get_application_context
from helium.selenium_wrappers import WebElement
from selenium.common.exceptions import NoSuchFrameException, \
	ElementNotVisibleException, UnexpectedAlertPresentException, \
	NoAlertPresentException, StaleElementReferenceException
from selenium.webdriver.common.alert import Alert as SeleniumAlert
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from threading import Thread
from time import time, sleep
from util.dictionary import inverse
from util.xpath import lower
import logging

_LOG = logging.getLogger(__name__)
_LOG.setLevel(logging.INFO)

DesiredCapabilities.FIREFOX["unexpectedAlertBehaviour"] = "ignore"

def start_firefox(url=None, firefox_profile=None):
	"""
	:param url: URL to open.
	:type url: str
	:param firefox_profile: Selenium\'s Firefox profile.
	:type firefox_profile: selenium.webdriver.firefox.firefox_profile.\
FirefoxProfile

	Starts the Firefox web browser and opens the specified URL, if provided.
	For instance::

		start_firefox("http://www.google.com/")
	"""
	return _get_api_impl().start_firefox(url, firefox_profile)

def start_chrome(url=None):
	"""
	:param url: URL to open.
	:type url: str

	Starts the Chrome web browser and opens the specified URL, if provided.
	For instance::

		start_chrome("http://www.google.com/")
	"""
	return _get_api_impl().start_chrome(url)

def start_ie(url=None):
	"""
	:param url: URL to open.
	:type url: str

	Starts the Internet Explorer web browser and opens the specified URL,
	if provided. For instance::

		start_ie("http://www.google.com/")
	"""
	return _get_api_impl().start_ie(url)

def go_to(url):
	"""
	:param url: URL to open.
	:type url: str

	Opens the specified URL in the current web browser window. For instance::

		go_to("www.google.com")
	"""
	_get_api_impl().go_to(url)

def set_driver(driver):
	"""
	Sets the Selenium driver.
	"""
	_get_api_impl().set_driver(driver)

def get_driver():
	"""
	Returns currently used Selenium driver object.
	"""
	return _get_api_impl().get_driver()

@decorator
def might_spawn_window(f, *args, **kwargs):
	if _get_api_impl().driver.is_ie() and Alert().exists():
		# Accessing .window_handles in IE when an alert is present raises an
		# UnexpectedAlertPresentException. When DesiredCapability
		# 'unexpectedAlertBehaviour' is not 'ignore' (the default is 'dismiss'),
		# this leads to the alert being closed. Since we don't want to
		# unintentionally close alert dialogs, we therefore do not access
		# .window_handles in IE when an alert is present.
		return f(*args, **kwargs)
	window_handles_before = _get_api_impl().driver.window_handles[:]
	result = f(*args, **kwargs)
	# As above, don't access .window_handles in IE if an alert is present:
	if not (_get_api_impl().driver.is_ie() and Alert().exists()):
		new_window_handles = [
			h for h in _get_api_impl().driver.window_handles
			if h not in window_handles_before
		]
		if new_window_handles:
			_get_api_impl().driver.switch_to_window(
				new_window_handles[0]
			)
	return result

@might_spawn_window
def write(text, into=None):
	"""
	:param text: The text to be written.
	:type text: one of (str, unicode)
	:param into: Name or label of a text field to write into.
	:type into: one of (str, unicode)

	Types the given text into the active window. If parameter 'into' is given,
	first sets the focus to the text field with name or label specified by this
	parameter. Common examples of 'write' are::

		write("Hello World!")
		write("user12345", into="Username:")
	"""
	_get_api_impl().write(text, into)

@might_spawn_window
def press(*keys):
	"""
	:param \*keys: Key or comma separated list of keys to be pressed.

	Presses the given keys in sequence. To press a normal letter key such as 'a'
	simply call `press` for that character::

		press('a')

	You can also simulate the pressing of upper case characters that way::

		press('A')

	To press a special key such as ENTER look it up in the list below, then
	call `press` for it::

		press(ENTER)

	To press multiple keys at the same time, concatenate them with `+`. For
	example, to press CTRL + a, call::

		press(CTRL + 'a')

	To press multiple key combinations in sequence, separate them by commas::

		press(ALT + 'f', 's')

	**List of non-letter keys:**

	* Common keys:
		``ENTER``, ``SPACE``, ``TAB``, ``ESC``
	* Modifiers:
		``CTRL``, ``ALT``, ``SHIFT``
	* Insertion / Deletion:
		``INS``, ``BKSP``, ``DEL``, ``END``
	* Navigation:
		``HOME``, ``END``, ``PGUP``, ``PGDN``
	* Arrows:
		``LEFT``, ``DOWN``, ``RIGHT``, ``UP``
	* Other keys above the arrow keys:
		``BREAK``, ``PAUSE``
	* Function keys:
		``F1``, ``F2``, ..., ``F12``
	* Numpad operations:
		``ADD``, ``SUBTRACT``, ``MULTIPLY``, ``DIVIDE``,
	* Numpad numbers:
		``NUMPAD0``, ``NUMPAD1``, ..., ``NUMPAD9``
	* Other numpad keys:
		``DECIMAL``
	* Left/right variants of other keys:
		``LSHIFT``,  ``LCTRL``
	* Others:
		``CLEAR``, ``HELP``, ``SEPARATOR``
	"""
	_get_api_impl().press(*keys)

ENTER = Keys.ENTER
SPACE = Keys.SPACE
TAB = Keys.TAB
ESC = Keys.ESCAPE
CTRL = Keys.CONTROL
ALT = Keys.ALT
SHIFT = Keys.SHIFT
INS = Keys.INSERT
BKSP = Keys.BACK_SPACE
DEL = Keys.DELETE
END = Keys.END
HOME = Keys.HOME
PGUP = Keys.PAGE_UP
PGDN = Keys.PAGE_DOWN
LEFT = Keys.ARROW_LEFT
DOWN = Keys.ARROW_DOWN
RIGHT = Keys.ARROW_RIGHT
UP = Keys.ARROW_UP
BREAK = Keys.CANCEL
PAUSE = Keys.PAUSE
F1 = Keys.F1
F2 = Keys.F2
F3 = Keys.F3
F4 = Keys.F4
F5 = Keys.F5
F6 = Keys.F6
F7 = Keys.F7
F8 = Keys.F8
F9 = Keys.F9
F10 = Keys.F10
F11 = Keys.F11
F12 = Keys.F12
ADD = Keys.ADD
SUBTRACT = Keys.SUBTRACT
MULTIPLY = Keys.MULTIPLY
DIVIDE = Keys.DIVIDE
NUMPAD0 = Keys.NUMPAD0
NUMPAD1 = Keys.NUMPAD1
NUMPAD2 = Keys.NUMPAD2
NUMPAD3 = Keys.NUMPAD3
NUMPAD4 = Keys.NUMPAD4
NUMPAD5 = Keys.NUMPAD5
NUMPAD6 = Keys.NUMPAD6
NUMPAD7 = Keys.NUMPAD7
NUMPAD8 = Keys.NUMPAD8
NUMPAD9 = Keys.NUMPAD9
DECIMAL = Keys.DECIMAL
LSHIFT = Keys.LEFT_SHIFT
LCTRL = Keys.LEFT_CONTROL
CLEAR = Keys.CLEAR
HELP = Keys.HELP
SEPARATOR = Keys.SEPARATOR

@might_spawn_window
def click(*elements):
	"""
	:param \*elements: Comma-separated list of GUI elements, labels (strings) \
or points.

	Clicks on the given elements in sequence. Common examples are::

		click("Close")
		click("File", "Save")
		click("File", MenuItem("Save"))
		click(Button("OK"))
		click(Point(200, 300))
		click(ComboBox("File type").center + (50, 0))

	Strings passed as parameters are automatically wrapped as :py:class:`Text`
	objects (so ``click("Helium")`` is equivalent to ``click(Text("Helium"))``).
	"""
	_get_api_impl().click(*elements)

@might_spawn_window
def doubleclick(element):
	"""
	:param element: A GUI element, label (string) or point.

	Performs a double-click on the given element. For example::

		doubleclick("Link")
		doubleclick(ListItem("Directories"))
		doubleclick(Point(200, 300))
		doubleclick(TextField("Username:").center - (0, 20))

	Strings passed as parameters are automatically wrapped as :py:class:`Text`
	objects (so ``doubleclick("Helium")`` is equivalent to
	``doubleclick(Text("Helium"))``).
	"""
	_get_api_impl().doubleclick(element)

@might_spawn_window
def drag(element, to):
	"""
	:param element: The element to drag.
	:param to: The element or Point to drag to.

	Drags the given GUI element to the given location. For example::

		drag("File", to="Folder")

	Both parameters "element" and "to" can be of any type that you can pass to
	:py:func:`helium.api.click`.

	The dragging is performed by hovering the mouse cursor over "element",
	pressing and holding the left mouse button, moving the mouse cursor over
	"to", and then releasing the left mouse button again.
	"""
	_get_api_impl().drag(element, to)

@might_spawn_window
def press_mouse_on(element):
	_get_api_impl().press_mouse_on(element)

@might_spawn_window
def release_mouse_over(element):
	_get_api_impl().release_mouse_over(element)

def find_all(predicate):
	"""
	Lets you find all occurrences of the given GUI element predicate. For
	instance, the following statement returns a list of all buttons with label
	"Open"::

		find_all(Button("Open"))

	In a typical usage scenario, you want to pick out one of the occurrences
	returned by :py:func:`find_all`. In such cases, :py:func:`list.sort` can
	be very useful. For example, to find the leftmost "Open" button, you can
	write::

		buttons = find_all(Button("Open"))
		leftmost_button = sorted(buttons, key=lambda button: button.x)[0]
	"""
	return _get_api_impl().find_all(predicate)

def scroll_down(steps=1):
	"""
	Scrolls down the mouse wheel given number of steps.
	"""
	_get_api_impl().scroll_down(steps)

def scroll_up(steps=1):
	"""
	Scrolls up the mouse wheel given number of steps.
	"""
	_get_api_impl().scroll_up(steps)

def scroll_right(steps=1):
	"""
	Scrolls right the mouse wheel given number of steps.
	"""
	_get_api_impl().scroll_right(steps)

def scroll_left(steps=1):
	"""
	Scrolls left the mouse wheel given number of steps.
	"""
	_get_api_impl().scroll_left(steps)


@might_spawn_window
def hover(*elements):
	"""
	:param \*elements: Comma-separated list of GUI elements, labels (strings) \
or points.

	Consecutively hovers the mouse cursor over the given elements. For example::

		hover("Close")
		hover(Button("OK"))
		hover("Home", "Download", "Start")
		hover("Home", MenuItem("Download"), "Start")
		hover(Point(200, 300))
		hover(ComboBox("File type").center + (50, 0))

	Strings passed as parameters are automatically wrapped as :py:class:`Text`
	objects (so ``hover("Helium")`` is equivalent to ``hover(Text("Helium"))``).
	"""
	_get_api_impl().hover(*elements)

@might_spawn_window
def rightclick(element, select=None, then_select=None, *finally_select):
	"""
	:param element: The GUI element, label (string) or point to right-click.
	:param select: GUI element, label (string) or point to left-click \
immediately after performing the right-click.
	:param then_select: GUI element, label (string) or point to left-click \
after clicking the ``select`` element.
	:param \*finally_select: Comma-separated list of GUI elements, labels \
(strings) and points to left-click after clicking the ``select`` and \
``then_select`` elements

	Performs a right click on the given element, optionally clicking on the
	specified sequence of context menu elements afterwards. For example::

		rightclick("Something", select="Menu Item")

	Strings passed as parameters are automatically wrapped as :py:class:`Text`
	objects (so ``rightclick("Helium")`` is equivalent to
	``rightclick(Text("Helium"))``).
	"""
	_get_api_impl().rightclick(
		element, select=select, then_select=then_select, *finally_select
	)

@might_spawn_window
def select(combo_box, value):
	"""
	Selects specified value from a combo box. For example::

		select("Language", "English")
		select(ComboBox("Language"), "English")
	"""
	_get_api_impl().select(combo_box, value)

def drag_file(file_path, to):
	"""
	Drags a file from local computer over an HTML element specified by its name
	and drops it there. This allows, for example, to attach files to emails in
	Gmail:

		click("COMPOSE")
		write("example@gmail.com", into="To")
		write("Email subject", into="Subject")
		drag_file("C:\\Documents\\notes.txt", to="Drop files here")
	"""
	_get_api_impl().drag_file(file_path, to)

def attach_file(file_path, to):
	"""
	Allows uploading a file, from local computer, to the <input type="file" />
	element located on a website.
	"""
	_get_api_impl().attach_file(file_path, to)

def wait_until(condition_fn, timeout_secs=10, interval_secs=0.5):
	"""
	Waits until the given condition function evaluates to true. This is most
	commonly used to wait for a GUI element to exist::

		wait_until(Text("Finished!").exists)

	When the optional parameter ``timeout_secs`` is given and not ``None``,
	``wait_until`` raises :py:class:`TimeoutExpired` if the condition is not
	satisfied within the given number of seconds. The parameter
	``interval_secs`` specifies the number of seconds Helium waits between
	evaluating the condition function.
	"""
	_get_api_impl().wait_until(condition_fn, timeout_secs, interval_secs)

class Config(object):
	"""
	This class contains Helium's run-time configuration. To modify Helium's
	behaviour, simply assign to the properties of this class. For instance::

		Config.auto_wait_enabled = False
	"""
	auto_wait_enabled = True
	"""
	When auto-wait is enabled, Helium automatically waits after performing
	GUI actions, such as :py:func:`press`, :py:func:`click` or :py:func:`write`.
	The amount of time waited is calculated dynamically. This can sometimes
	lead to wait intervals that are too long. To speed up the execution of your
	scripts, the property ``auto_wait_enabled`` can therefore be used to disable
	Helium's automatic wait facility.

	You can disable or enable Helium's auto-wait at any point in your script.
	For example::

		>>> Config.auto_wait_enabled = False
		>>> write("John", into="Name")
		>>> press(TAB)
		>>> write("Smith")
		>>> Config.auto_wait_enabled = True
		>>> click("Submit")
	"""
	search_timeout_secs = 10
	"""
	Amount of time (in seconds) Helium attempts to find a GUI element for.
	If the search does not succeed within the time defined by this configuration
	value, Automa raises :py:class:`TimeoutExpired`. Increasing the property of
	this value can be useful on lower-spec computers.
	"""

class GUIElement(object):
	"""
	Base class for all Helium's GUI elements.
	"""
	def __init__(self):
		self._first_occurrence = None
	def exists(self):
		"""
		Evaluates to true if this GUI element exists.
		"""
		try:
			next(self.find_all())
		except StopIteration:
			return False
		else:
			return True
	def find_all(self):
		return self.find_all_in(_get_api_impl().driver)
	def find_all_in(self, driver):
		raise NotImplementedError()
	def with_occurrence(self, occurrence):
		result = copy(self)
		# It's OK to access the protected member as it's ours anyways:
		# pylint: disable=W0212
		result._first_occurrence = occurrence
		# pylint: enable=W0212
		return result
	@property
	def first_occurrence(self):
		if self._first_occurrence is None:
			self._set_first_occurrence()
		return self._first_occurrence
	def _set_first_occurrence(self):
		self._first_occurrence = self.find()
	def find(self):
		return self.perform(lambda _: None)
	def perform(self, action, ignored_exceptions=(ElementNotVisibleException,)):
		end_time = time() + Config.search_timeout_secs
		# Try to perform `action` at least once:
		result = self._perform_no_wait(action, ignored_exceptions)
		while result is None and Config.auto_wait_enabled and time() < end_time:
			result = self._perform_no_wait(action, ignored_exceptions)
		if result is not None:
			return result
		raise LookupError()
	def _perform_no_wait(self, action, ignored_exceptions):
		for element in self.find_all():
			try:
				action(element)
				return element
			except ignored_exceptions:
				pass

class HTMLElement(GUIElement):
	"""
	This class defines properties that are available for all of Helium's GUI
	(HTML) elements.

	One feature that all of Helium's GUI elements support are the optional
	arguments ``below=``, ``to_right_of=``, ``above=`` and ``to_left_of=``.
	These arguments specify where a particular GUI element is to be searched
	for. For example::

		Button("OK", to_left_of="Cancel")

	This identifies the Button to the left of text "Cancel". Being able to
	restrict the search region for a GUI element like this can be useful for
	disambiguating multiple occurrences of a GUI element, especially when the
	occurrences are arranged in a table.

	Relative GUI element searches can be nested and combined arbitrarily with
	Helium's other functions. For example::

		click(Button("Log in", to_right_of=TextField("Username:")))

	This clicks on the button with text "Log in" to the right of text field
	"Username:".
	"""
	def __init__(
			self, below=None, to_right_of=None, above=None, to_left_of=None
	):
		super(HTMLElement, self).__init__()
		self.below = Text(below) if isinstance(below, basestring) else below
		self.to_right_of = Text(to_right_of) if \
			isinstance(to_right_of, basestring) else to_right_of
		self.above = Text(above) if isinstance(above, basestring) else above
		self.to_left_of = Text(to_left_of) if \
			isinstance(to_left_of, basestring) else to_left_of
	@property
	def width(self):
		"""
		The width of this UI element.
		"""
		return self.first_occurrence.location.width
	@property
	def height(self):
		"""
		The height of this UI element.
		"""
		return self.first_occurrence.location.height
	@property
	def x(self):
		"""
		The x-coordinate of the top-left point of this UI element.
		"""
		return self.first_occurrence.location.left
	@property
	def y(self):
		"""
		The y-coordinate of the top-left point of this UI element.
		"""
		return self.first_occurrence.location.top
	@property
	def center(self):
		"""
		The center of this UI element, as a :py:class:`helium.api.Point`.
		"""
		loc = self.first_occurrence.location
		return Point(loc.left + loc.width / 2, loc.top + loc.height / 2)
	def find_all_in(self, driver):
		for occurrence in self.find_all_in_search_regions(driver):
			if occurrence.is_displayed():
				yield occurrence
		for iframe in driver.find_elements_by_tag_name('iframe'):
			try:
				driver.switch_to_frame(iframe.get_attribute('id'))
			except (NoSuchFrameException, StaleElementReferenceException):
				continue
			else:
				for occurrence in self.find_all_in_search_regions(driver):
					if occurrence.is_displayed():
						yield occurrence
				driver.switch_to_default_content()
	def find_all_in_search_regions(self, driver):
		search_regions = self._get_search_regions(driver)
		for occurrence in self.find_all_in_curr_frame(driver):
			if self._is_in_any_search_region(occurrence, search_regions):
				yield occurrence
	def _get_search_regions(self, driver):
		result = []
		if self.below:
			result.append(map(
				lambda elt: elt.location.is_above,
				self.below.find_all_in_curr_frame(driver)
			))
		if self.to_right_of:
			result.append(map(
				lambda elt: elt.location.is_to_left_of,
				self.to_right_of.find_all_in_curr_frame(driver)
			))
		if self.above:
			result.append(map(
				lambda elt: elt.location.is_below,
				self.above.find_all_in_curr_frame(driver)
			))
		if self.to_left_of:
			result.append(map(
				lambda elt: elt.location.is_to_right_of,
				self.to_left_of.find_all_in_curr_frame(driver)
			))
		return result
	def _is_in_any_search_region(self, element, search_regions):
		for direction in search_regions:
			found = False
			for search_region in direction:
				if search_region(element.location):
					found = True
					break
			if not found:
				return False
		return True
	def find_all_in_curr_frame(self, driver):
		raise NotImplementedError()
	def _is_enabled(self):
		"""
		Useful for subclasses.
		"""
		return not self.first_occurrence.get_attribute('disabled')

class MatchType(object):
	@staticmethod
	def PREFIX_IGNORE_CASE(value, text):
		if not text:
			return ''
		# Asterisks '*' are sometimes used to mark required fields. Eg.:
		# <label for="title"><span class="red-txt">*</span> Title:</label>
		# The starts-with filter below would be too strict to include such
		# matches. To get around this, we ignore asterisks unless the searched
		# text itself contains one.
		if '*' in text:
			strip_asterisks = value
		else:
			strip_asterisks = "translate(%s, '*', '')" % value
		return "[starts-with(normalize-space(%s), '%s')]" % (
			lower(strip_asterisks), text.lower()
		)

class HTMLElementIdentifiedByXPath(HTMLElement):
	def find_all_in_curr_frame(self, driver):
		x_path = self.get_xpath(MatchType.PREFIX_IGNORE_CASE)
		_LOG.debug("Looking for HTML element using xpath: %s." % x_path)
		return self._sort_search_result(
			map(WebElement, driver.find_elements_by_xpath(x_path)), driver
		)
	def _sort_search_result(self, search_result, driver):
		keys_to_result_items = []
		for web_elt in search_result:
			try:
				key = self.get_sort_index(driver, web_elt)
			except StaleElementReferenceException:
				pass
			else:
				keys_to_result_items.append((key, web_elt))
		keys_to_result_items.sort(key=lambda (sort_key, result_item): sort_key)
		return map(lambda (key, result_item): result_item, keys_to_result_items)
	def get_xpath(self, match_type):
		raise NotImplementedError()
	def get_sort_index(self, driver, web_element):
		return driver.get_distance_to_last_manipulated(web_element) + 1

class ClickableText(HTMLElementIdentifiedByXPath):
	def __init__(self, text, **kwargs):
		super(ClickableText, self).__init__(**kwargs)
		self.text = text
	def get_xpath(self, match_type):
		return Text(self.text).get_xpath(match_type) + ' | ' + \
			   Button(self.text).get_xpath(match_type) + ' | ' + \
			   Image(self.text).get_xpath(match_type)
	def get_sort_index(self, driver, web_element):
		sort_group = 2
		if web_element.tag_name == 'input':
			sort_group = 1
		if web_element.tag_name == 'img':
			sort_group = 3
		return sort_group * \
			   super(ClickableText, self).get_sort_index(driver, web_element)

class HTMLElementContainingText(HTMLElementIdentifiedByXPath):
	def __init__(self, element_type, text=None, **kwargs):
		super(HTMLElementContainingText, self).__init__(**kwargs)
		self.element_type = element_type
		self.search_text = text
	def get_xpath(self, matches):
		xpath_base = "//%s%s" % (
			self.element_type, matches('.', self.search_text)
		)
		return '%s[not(self::script)][not(.%s)]' % (xpath_base, xpath_base)

class Text(HTMLElementContainingText):
	"""
	Lets you identify any text or label. This is most useful for checking
	whether a particular text is shown on the screen::

		Text("Hello World!").exists()

	For an explanation of the parameters ``below``, ``to_right_of``, ``above``
	and ``to_left_of``, please see the documentation of :py:class:`HTMLElement`.
	"""
	def __init__(self, text=None, **kwargs):
		super(Text, self).__init__('*', text, **kwargs)
	@property
	def value(self):
		"""
		Returns the current value of this Text object.
		"""
		return self.first_occurrence.text
	def get_xpath(self, matches):
		return super(Text, self).get_xpath(matches) + ' | ' + \
			   Button(self.search_text).get_submit_button_xpath(matches) + \
			   ' | ' + Link(self.search_text).get_xpath(matches) + \
			   ' | //text()%s/..' % matches('.', self.search_text)

class Link(HTMLElementContainingText):
	"""
	Lets you identify a link (<a></a> HTML element). For example::

		Link("Next").exists()

	For an explanation of the parameters ``below``, ``to_right_of``, ``above``
	and ``to_left_of``, please see the documentation of :py:class:`HTMLElement`.
	"""
	def __init__(self, text=None, **kwargs):
		super(Link, self).__init__('a', text, **kwargs)
	def get_xpath(self, matches):
		return super(Link, self).get_xpath(matches) + ' | ' + \
			   "//a%s" % matches('@title', self.search_text)

class Label(HTMLElementContainingText):
	"""
	Lets you identify a label (<label></label> HTML element). For example::

		Label("User name").exists()

	For an explanation of the parameters ``below``, ``to_right_of``, ``above``
	and ``to_left_of``, please see the documentation of :py:class:`HTMLElement`.
	"""
	def __init__(self, text=None, **kwargs):
		super(Label, self).__init__('label', text, **kwargs)

class ListItem(HTMLElementContainingText):
	"""
	Lets you identify a list item by its name (<li></li> HTML element).

	For an explanation of the parameters ``below``, ``to_right_of``, ``above``
	and ``to_left_of``, please see the documentation of :py:class:`HTMLElement`.
	"""
	def __init__(self, text=None, **kwargs):
		super(ListItem, self).__init__('li', text, **kwargs)

class Button(HTMLElementContainingText):
	"""
	Lets you identify a button by its name and read its properties.
	An example usage of 'Button' is::

		Button("Log In").exists()

	This will look for the HTML button with the 'Log In' label::

		<button>Log in</button>

	and will return True if found, False otherwise.

	For an explanation of the parameters ``below``, ``to_right_of``, ``above``
	and ``to_left_of``, please see the documentation of :py:class:`HTMLElement`.
	"""
	def __init__(self, text=None, **kwargs):
		super(Button, self).__init__('button', text, **kwargs)
	def is_enabled(self):
		"""
		Returns true if this UI element can currently be interacted with.
		"""
		aria_disabled = self.first_occurrence.get_attribute('aria-disabled')
		return self._is_enabled() \
			and (not aria_disabled or aria_disabled.lower() == 'false')
	def get_xpath(self, matches):
		has_aria_label = matches('@aria-label', self.search_text)[1:-1]
		has_text = matches('.', self.search_text)[1:-1]
		return ' | '.join([
			super(Button, self).get_xpath(matches),
			self.get_submit_button_xpath(matches),
			"//div[@role='button'][%s or %s]" % (has_aria_label, has_text),
			"//button%s" % matches('@aria-label', self.search_text)
		])
	def get_submit_button_xpath(self, matches):
		if self.search_text:
			has_value = matches('@value', self.search_text)[1:-1]
			has_label = matches('@label', self.search_text)[1:-1]
			has_aria_label = matches('@aria-label', self.search_text)[1:-1]
			has_text = "[%s or %s or %s]" % (
				has_value, has_label, has_aria_label
			)
		else:
			has_text = ''
		return "//input[@type='submit']" + has_text

class Image(HTMLElementIdentifiedByXPath):
	"""
	Lets you identifier an image (<img /> HTML element) by its alt parameter.

	For an explanation of the parameters ``below``, ``to_right_of``, ``above``
	and ``to_left_of``, please see the documentation of :py:class:`HTMLElement`.
	"""
	def __init__(self, alt, **kwargs):
		super(Image, self).__init__(**kwargs)
		self.alt = alt
	def get_xpath(self, matches):
		return "//img%s" % matches('@alt', self.alt)

class LabelledElement(HTMLElement):
	SECONDARY_SEARCH_DIMENSION_PENALTY_FACTOR = 1.5
	def __init__(self, label=None, **kwargs):
		super(LabelledElement, self).__init__(**kwargs)
		self.label = label
	def find_all_in_curr_frame(self, driver):
		all_elts = \
			map(WebElement, driver.find_elements_by_xpath(self.get_xpath()))
		if self.label is None:
			result = all_elts
		else:
			labels = Label(self.label).find_all_in_curr_frame(driver) or \
					 Text(self.label).find_all_in_curr_frame(driver)
			result = \
				list(self._filter_elts_belonging_to_labels(all_elts, labels))
		return sorted(result, key=driver.get_distance_to_last_manipulated)
	def get_xpath(self):
		raise NotImplementedError()
	def get_primary_search_direction(self):
		return 'to_right_of'
	def get_secondary_search_direction(self):
		return 'below'
	def _filter_elts_belonging_to_labels(self, all_elts, labels):
		for label, elt in self._get_labels_with_explicit_elts(all_elts, labels):
			yield elt
			labels.remove(label)
			all_elts.remove(elt)
		labels_to_elts = self._get_related_elts(all_elts, labels)
		labels_to_elts = self._ensure_at_most_one_label_per_elt(labels_to_elts)
		self._retain_closest(labels_to_elts)
		for elts_for_label in labels_to_elts.values():
			assert len(elts_for_label) <= 1
			if elts_for_label:
				yield next(iter(elts_for_label))
	def _get_labels_with_explicit_elts(self, all_elts, labels):
		for label in labels:
			if label.tag_name == 'label':
				label_target = label.get_attribute('for')
				if label_target:
					for elt in all_elts:
						elt_id = elt.get_attribute('id')
						if elt_id.lower() == label_target.lower():
							yield label, elt
	def _get_related_elts(self, all_elts, labels):
		result = {}
		for label in labels:
			for elt in all_elts:
				if self._are_related(elt, label):
					if label not in result:
						result[label] = set()
					result[label].add(elt)
		return result
	def _are_related(self, elt, label):
		if elt.location.intersects(label.location):
			return True
		prim_search_dir = self.get_primary_search_direction()
		sec_search_dir = self.get_secondary_search_direction()
		if label.location.distance_to(elt.location) <= 150 and (
			elt.location.is_in_direction(prim_search_dir, label.location) or
			elt.location.is_in_direction(sec_search_dir, label.location)
		):
			return True
		return False
	def _ensure_at_most_one_label_per_elt(self, labels_to_elts):
		elts_to_labels = inverse(labels_to_elts)
		self._retain_closest(elts_to_labels)
		return inverse(elts_to_labels)
	def _retain_closest(self, pivots_to_elts):
		for pivot, elts in pivots_to_elts.items():
			if elts:
				pivots_to_elts[pivot] = {self._find_closest(pivot, elts)}
	def _find_closest(self, to_pivot, among_elts):
		remaining_elts = iter(among_elts)
		result = next(remaining_elts)
		result_distance = self._compute_distance(result, to_pivot)
		for element in remaining_elts:
			element_distance = self._compute_distance(element, to_pivot)
			if element_distance < result_distance:
				result = element
				result_distance = element_distance
		return result
	def _compute_distance(self, elt_1, elt_2):
		loc_1 = elt_1.location
		loc_2 = elt_2.location
		if loc_1.is_in_direction(self.get_secondary_search_direction(), loc_2):
			factor = self.SECONDARY_SEARCH_DIMENSION_PENALTY_FACTOR
		else:
			factor = 1
		return factor * loc_1.distance_to(loc_2)

class CompositeElement(HTMLElement):
	def __init__(self, *args, **kwargs):
		super(CompositeElement, self).__init__(**kwargs)
		self.args = args
		self.kwargs = kwargs
		self._first_element = self._first_elt_of_last_search = None
	@property
	def first_element(self):
		if self._first_element is None:
			self._set_first_occurrence()
			# find_all_in_curr_frame(...) now sets _first_elt_of_last_search
			self._first_element = self._first_elt_of_last_search
		return self._first_element
	def find_all_in_curr_frame(self, driver):
		already_yielded = []
		for element in self.get_elements():
			for occurrence in element.find_all_in_curr_frame(driver):
				if occurrence not in already_yielded:
					if not already_yielded:
						self._first_elt_of_last_search = \
							element.with_occurrence(occurrence)
					yield occurrence
					already_yielded.append(occurrence)
	def get_elements(self):
		for element_type in self.get_element_types():
			yield element_type(*self.args, **self.kwargs)
	def get_element_types(self):
		raise NotImplementedError()

class TextField(CompositeElement):
	"""
	Lets you identify a text field on the web page (<input /> or <textarea />
	HTML elements). For example::

		TextField("File name").value

	This returns the value of the "File name" text field. If it is empty, the
	empty string '' is returned.

	For an explanation of the parameters ``below``, ``to_right_of``, ``above``
	and ``to_left_of``, please see the documentation of :py:class:`HTMLElement`.
	"""
	def __init__(self, label=None, **kwargs):
		super(TextField, self).__init__(label, **kwargs)
	def get_element_types(self):
		return [
			StandardTextFieldWithLabel, AriaTextFieldWithLabel,
			StandardTextFieldWithPlaceholder
		]
	@property
	def value(self):
		"""
		Returns the current value of this text field. '' if there is no value.
		"""
		return self.first_element.value
	def is_enabled(self):
		"""
		Returns true if this UI element can currently be interacted with.
		"""
		return self.first_element.is_enabled()
	def is_readonly(self):
		"""
		Returns true if the value of this UI element cannot be modified.
		"""
		return self.first_element.is_readonly()

class StandardTextFieldWithLabel(LabelledElement):
	@property
	def value(self):
		return self.first_occurrence.get_attribute('value') or ''
	def is_enabled(self):
		return self._is_enabled()
	def is_readonly(self):
		return bool(self.first_occurrence.get_attribute('readOnly'))
	def get_xpath(self):
		return \
			"//input[@type='text' or @type='email' or @type='password' " \
			"or @type='number' or string-length(@type)=0] | //textarea"

class AriaTextFieldWithLabel(LabelledElement):
	@property
	def value(self):
		return self.first_occurrence.text
	def is_enabled(self):
		return self._is_enabled()
	def is_readonly(self):
		return bool(self.first_occurrence.get_attribute('readOnly'))
	def get_xpath(self):
		return "//body[@role='textbox'] | //div[@role='textbox']"

class StandardTextFieldWithPlaceholder(HTMLElementIdentifiedByXPath):
	def __init__(self, label, **kwargs):
		super(StandardTextFieldWithPlaceholder, self).__init__(**kwargs)
		self.label = label
	@property
	def value(self):
		return self.first_occurrence.get_attribute('value') or ''
	def is_enabled(self):
		return self._is_enabled()
	def is_readonly(self):
		return bool(self.first_occurrence.get_attribute('readOnly'))
	def get_xpath(self, matches):
		return "(%s)%s" % (
			StandardTextFieldWithLabel(self.label).get_xpath(),
			matches('@placeholder', self.label)
		)

class FileInput(LabelledElement):
	def get_xpath(self):
		return "//input[@type='file']"

class ComboBox(LabelledElement):
	"""
	Lets you identify a combo box and read its properties and options. Eg.::

		ComboBox("Language").exists()

	This looks for a combo box with label 'Language' and returns True if found,
	False otherwise.

	For an explanation of the parameters ``below``, ``to_right_of``, ``above``
	and ``to_left_of``, please see the documentation of :py:class:`HTMLElement`.
	"""
	def is_readonly(self):
		"""
		Returns True if the value of this GUI element cannot be modified.
		"""
		return self.first_occurrence.tag_name == 'select'
	def get_xpath(self):
		return "//select | //input[@type='text' and @list]"

class CheckBox(LabelledElement):
	"""
	Lets you identify a check box (<input type="checkbox" /> HTML element) by
	its name or label and read its properties::

		CheckBox("I agree").exists()

	This looks for a check box with label 'I agree' and returns True if found,
	False otherwise.

	For an explanation of the parameters ``below``, ``to_right_of``, ``above``
	and ``to_left_of``, please see the documentation of :py:class:`HTMLElement`.
	"""
	def is_enabled(self):
		"""
		Returns True if this GUI element can currently be interacted with.
		"""
		return self._is_enabled()
	def is_checked(self):
		"""
		Returns True if this GUI element is checked (selected).
		"""
		return bool(self.first_occurrence.get_attribute('checked'))
	def get_xpath(self):
		return "//input[@type='checkbox']"
	def get_primary_search_direction(self):
		return 'to_left_of'
	def get_secondary_search_direction(self):
		return 'to_right_of'

class RadioButton(LabelledElement):
	"""'
	Lets you identify a radio button (<input type="radio" /> HTML element) by
	name or label and read its properties. To for instance check whether a radio
	button is currently selected, use::

		RadioButton("Option 2").is_selected()

	For an explanation of the parameters ``below``, ``to_right_of``, ``above``
	and ``to_left_of``, please see the documentation of :py:class:`HTMLElement`.
	"""
	def is_selected(self):
		"""
		Returns true if this radio button is selected.
		"""
		return bool(self.first_occurrence.get_attribute('checked'))
	def get_xpath(self):
		return "//input[@type='radio']"
	def get_primary_search_direction(self):
		return 'to_left_of'
	def get_secondary_search_direction(self):
		return 'to_right_of'

class Window(GUIElement):
	"""
	Lets you identify a window by its title.
	"""
	def __init__(self, title=None):
		super(Window, self).__init__()
		self._title = title
	def find_all_in(self, driver):
		for handle in driver.window_handles:
			window = SeleniumWindow(driver, handle)
			if self._title is None or window.title.startswith(self._title):
				yield window
	@property
	def title(self):
		"""
		Returns the title of this Window.
		"""
		return self.first_occurrence.title
	@property
	def handle(self):
		"""
		Returns the Windows Operating System handle (HWND) assigned to this
		window.
		"""
		return self.first_occurrence.handle

class SeleniumWindow(object):
	def __init__(self, driver, handle):
		self.driver = driver
		self.handle = handle
		self._window_handle_before = None
	@property
	def size(self):
		with self:
			return self.driver.get_window_size()
	@property
	def location(self):
		with self:
			return self.driver.get_window_position()
	@property
	def title(self):
		with self:
			return self.driver.title
	def __enter__(self):
		self._window_handle_before = self.driver.current_window_handle
		if self.driver.current_window_handle != self.handle:
			self.driver.switch_to_window(self.handle)
	def __exit__(self, *_):
		if self.driver.current_window_handle != self._window_handle_before:
			self.driver.switch_to_window(self._window_handle_before)

class Alert(GUIElement):
	"""
	Lets you identify and interact with Javascript alert boxes.
	"""
	def __init__(self, text=None):
		super(Alert, self).__init__()
		self._text = text
	def find_all_in(self, driver):
		result = driver.switch_to_alert()
		try:
			text = result.text
			if self._text is None or text.startswith(self._text):
				yield result
		except NoAlertPresentException:
			pass
	@property
	def text(self):
		"""
		Text displayed in the alert box.
		"""
		return self.first_occurrence.text
	def _click(self, *elements):
		if len(elements) > 1:
			raise UnexpectedAlertPresentException(
				"In alert dialog %r, it is only possible to click one element."
				% self.text
			)
		element = elements[0]
		if element.lower() == 'ok':
			self._accept()
		elif element.lower() == 'cancel':
			self._dismiss()
		else:
			raise UnexpectedAlertPresentException(
				"In alert dialog %r, it is only possible to click('OK') or "
				"click('Cancel')." % self.text
			)
	def _write(self, text, into=None):
		if into:
			if isinstance(into, TextField):
				tf_label = into.args[0]
				if tf_label is None or tf_label not in self.text:
					raise LookupError(
						"Alert dialog %r does not contain a text field with "
						"label %r." % (self.text, tf_label)
					)
			elif isinstance(into, Alert) or isinstance(into, SeleniumAlert):
				if into.text != self.text:
					raise LookupError(
						"Alert dialog %r does not have expected text %r." %
						(self.text, into.text)
					)
		self._send_keys(text)
	def _send_keys(self, *keys):
		for key in keys:
			if key == ENTER:
				self._accept()
			elif key == ESC:
				self._dismiss()
			else:
				self.first_occurrence.send_keys(key)
	def _accept(self):
		self.first_occurrence.accept()
	def _dismiss(self):
		self.first_occurrence.dismiss()

class Point(namedtuple('Point', ['x', 'y'])):
	"""
	A clickable point. To create a ``Point`` at an offset of an existing point,
	use ``+`` and ``-``::

		>>> point = Point(x=10, y=25)
		>>> point + (10, 0)
		Point(x=20, y=25)
		>>> point - (0, 10)
		Point(x=10, y=15)
	"""
	def __new__(cls, x=0, y=0):
		return cls.__bases__[0].__new__(cls, x, y)
	def __init__(self, x=0, y=0):
		self.__class__.__bases__[0].__init__(self, seq=(x, y))
	@property
	def x(self):
		"""
		The x coordinate of the point.
		"""
		return self[0]
	@property
	def y(self):
		"""
		The y coordinate of the point.
		"""
		return self[1]
	def __eq__(self, other):
		return (self.x, self.y) == other
	def __ne__(self, other):
		return not self == other
	def __hash__(self):
		return self.x + 7 * self.y
	def __add__(self, (dx, dy)):
		return Point(self.x + dx, self.y + dy)
	def __radd__(self, (dx, dy)):
		return self.__add__((dx, dy))
	def __sub__(self, (dx, dy)):
		return Point(self.x - dx, self.y - dy)
	def __rsub__(self, (x, y)):
		return Point(x - self.x, y - self.y)

def switch_to(window):
	"""
	:param window: The title (string) of a window on screen or a \
:py:class:`Window` object

	Switches to the given window. For example::

		switch_to("Google")

	This searches for a window whose title contains "Google", and activates it.
	"""
	_get_api_impl().switch_to(window)

def kill(application):
	application.quit()

def highlight(element):
	"""
	:param element: The element to highlight.

	Highlights the given element on the webpage by drawing a red rectangle
	around it. For example::

		highlight(Text("Helium"))
	"""
	if hasattr(element, 'first_occurrence'):
		element = element.first_occurrence
	previous_style = element.style
	element.style = "border: 2px solid red; font-weight: bold;"
	def clear_highlighting():
		sleep(2)
		element.style = previous_style
	Thread(target=clear_highlighting).start()

def _get_api_impl():
	return get_application_context().get_object('APIImpl')