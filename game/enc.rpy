init python:

    class EventEmitter:
        def on(self, ev_name):
            """Decorator to register a new callback function to an event."""
            def wrapper(callback):
                self.callbacks[ev_name] = self.callbacks.get(ev_name, [])
                self.callbacks[ev_name].append(callback)

            return wrapper

        def emit(self, ev_name):  # type: (str) -> None
            """Emit an event, triggered every callback registered to it."""
            for callback in self.callbacks[ev_name]:
                callback(self)



    class EncyclopaediaAction(Action):
        """Base Action that requires an Encyclopaedia as an argument.

        Should only be used for class inheritance.

        Args:
            encyclopaedia (Encyclopaedia): The Encyclopaedia instance to use.
        """
        def __init__(self, encyclopaedia):
            self.enc = encyclopaedia


    class SetEntryAction(EncyclopaediaAction):
        """Set an Encyclopaedia entry as the active entry,
        then opens the Encyclopaedia's Entry Screen

        Used for opening entries directly with a button.

        Args:
            encyclopaedia (Encyclopaedia): The Encyclopaedia instance to use.
            entry (EncEntry): The entry to be made active.
        """
        def __init__(self, encyclopaedia, entry):
            super(SetEntryAction, self).__init__(encyclopaedia)

            self.entry = entry

        def set_entry(self):  # type: () -> None
            # Find the position of the entry
            if self.enc.show_locked_entry is False:
                target_position = self.enc.unlocked_entries.index(self.entry)
            else:
                target_position = self.enc.all_entries.index(self.entry)

            # The active entry is set to whichever list position was found.
            self.enc.active = self.entry

            if self.enc.active.locked is False:
                if self.entry.viewed is False:
                    # Run the callback, if provided.
                    self.entry.emit("viewed")
                # Mark the entry as viewed.
                self.enc.active.viewed = True

            self.enc.current_position = target_position

        def __call__(self):
            self.set_entry()

            # Show the entry screen associated with the encyclopaedia.
            renpy.show_screen(self.enc.entry_screen, self.enc)
            renpy.restart_interaction()


    class ChangeAction(EncyclopaediaAction):
        """Base Action that swaps an open entry/page for the previous or next one.

        Args:
            encyclopaedia (Encyclopaedia): The Encyclopaedia instance to use.
            direction (bool): The direction to go in. 0 for back, 1 for forward.
            block (bool): True if at the first or last entry
        """
        def __init__(self, encyclopaedia, direction, block):
            super(ChangeAction, self).__init__(encyclopaedia)

            # Determines if it's going to the previous or next entry.
            self.direction = direction

            # If the button is active or not.
            self.block = block

        def get_sensitive(self):  # type: () -> bool
            """Determines if the button should be alive or not.

            Returns:
                bool: True if the button should be alive, else False.
            """
            return not self.block


    class ChangeEntryAction(ChangeAction):
        """Change the current entry being viewed.

        Used for switching from one entry to another.

        Used by Encyclopaedia's PreviousEntry() and NextEntry() functions.
        """

        def get_entry(self):  # type: () -> EncEntry
            """Get the entry at the given index.

            If NOT showing locked entries, the next entry we want to see is
            the next entry in unlocked_entries.
            Else, the next entry we want is the next entry in all_entries.

            Returns:
                EncEntry
            """
            if self.enc.show_locked_entry is False:
                entry = self.enc.unlocked_entries[self.enc.current_position]
            else:
                entry = self.enc.all_entries[self.enc.current_position]

            return entry

        def __call__(self):
            if self.block is False:
                # Update the current position.
                self.enc.current_position += self.direction

                # Update the active entry.
                self.enc.active = self.get_entry()

                if self.enc.active.locked is False:
                    # Run the callback, if provided.
                    self.enc.active.emit("viewed")

                    # Mark the entry as viewed.
                    self.enc.active.viewed = True

                # When changing an entry, the current sub-entry page number is
                # set back to 1.
                self.enc.sub_current_position = 1
                self.enc.active.current_page = self.enc.sub_current_position

                renpy.restart_interaction()


    class ChangePageAction(ChangeAction):
        """Change the current sub-entry being viewed.

        Used for switching from one page to another.

        Used by an Encyclopaedia's PreviousPage() and NextPage() functions.
        """
        def __call__(self):
            if self.block is False:
                # The Encyclopaedia's page display changes.
                self.enc.sub_current_position += self.direction

                # The EncEntry's current page changes to match.
                self.enc.active.current_page = self.enc.sub_current_position

                if self.enc.active.current_page.viewed is False:
                    self.enc.active.current_page.viewed = True

                renpy.restart_interaction()


    class SortEncyclopaedia(EncyclopaediaAction):
        """Sorts the entries based on encyclopaedia.sorting_mode.

        Args:
            encyclopaedia (Encyclopaedia): The Encyclopaedia instance to use.
            sorting_mode (bool): The sorting mode to sort by.
        """
        def __init__(self, encyclopaedia, sorting_mode=0):
            super(SortEncyclopaedia, self).__init__(encyclopaedia)

            self.sorting_mode = sorting_mode

            self.reverse = False
            if sorting_mode == self.enc.SORT_REVERSE_ALPHABETICAL:
                self.reverse = True

        def __call__(self):
            self.enc.sort_entries(
                entries=self.enc.current_entries,
                sorting=self.sorting_mode,
                reverse=self.reverse
            )

            self.enc.sorting_mode = self.sorting_mode
            renpy.restart_interaction()

        def get_selected(self):
            return self.enc.sorting_mode == self.sorting_mode


    def _build_subject_filter(enc, subject):
        """Build an encyclopaedia's filtered_entries based on the subject given.

        Args:
            enc (Encyclopaedia): The encyclopaedia to filter.
            subject (str): The subject for the filter.
        """
        if enc.show_locked_buttons is False:
            entries = enc.unlocked_entries
        else:
            entries = enc.all_entries

        enc.filtered_entries = [i for i in entries if i.subject == subject]


    class FilterBySubject(EncyclopaediaAction):
        """Create a filter for entries, based on the given subject.
        """
        def __init__(self, encyclopaedia, subject):
            super(FilterBySubject, self).__init__(encyclopaedia)

            self.subject = subject

        def __call__(self):
            self.enc.filtering = self.subject

            _build_subject_filter(self.enc, self.subject)

            renpy.restart_interaction()

        def get_selected(self):
            self.selected = self.enc.filtering == self.subject
            return self.selected


    class ClearFilter(EncyclopaediaAction):
        """Stop filtering an Encyclopaedia.
        """
        def __call__(self):
            self.enc.filtering = False
            renpy.restart_interaction()


    class ResetSubPageAction(EncyclopaediaAction):
        """Resets the sub-page count to 1. Used when closing the entry screen.
        """
        def __call__(self):
            self.enc.sub_current_position = 1
            if self.enc.active is not None:
                self.enc.active.current_page = 1
            renpy.restart_interaction()


    class ToggleShowLockedButtonsAction(EncyclopaediaAction):
        """Toggles if locked Entries will be visible in the list of Entries.
        """
        def __call__(self):
            self.enc.show_locked_buttons = not self.enc.show_locked_buttons

            # Ensure the filtering isn't broken by hiding buttons.
            if self.enc.filtering:
                _build_subject_filter(self.enc, self.enc.filtering)

            # Ensure the sorting isn't broken by hiding buttons.
            reverse = False
            if self.enc.sorting_mode == self.enc.SORT_REVERSE_ALPHABETICAL:
                reverse = True

            self.enc.sort_entries(
                entries=self.enc.current_entries,
                sorting=self.enc.sorting_mode,
                reverse=reverse,
            )

            renpy.restart_interaction()


    class ToggleShowLockedEntryAction(EncyclopaediaAction):
        """Toggles if locked Entries can be viewed.
        """
        def __call__(self):
            self.enc.show_locked_entry = not self.enc.show_locked_entry
            renpy.restart_interaction()

    from operator import itemgetter




    class EncEntry(EventEmitter, store.object):
        """Stores an Entry's content.
        EncEntry instances should be added to an Encyclopaedia.

        Args:
            parent (Encyclopaedia, EncEntry)
            number (int) -
                The entry's number.
                If this is not set then it will be given a number automatically.
            name (str) -
                The name that will be displayed for the entry's button and labels.
            text (str, list) -
                The text that will be displayed when the entry is viewed.
            subject (str) -
                The subject to associate the entry with.
                Used for sorting and filtering.
            viewed (bool) -
                Determines if the entry has been seen or not.
                This should only be set if the Encyclopaedia is
                save-game independent.
            viewed_persistent(bool) -
                Determines if the Entry's viewed status uses persistent data.
            locked (bool) -
                Determines if the entry can be viewed or not. Defaults to False.
            locked_persistent(bool) -
                Determines if the Entry's locked status uses persistent data.
            image (str) -
                The image displayed with the Entry text. Default is None.
            locked_name (str) -
                Placeholder text for the name. Shown when the entry is locked.
            locked_text (str) -
                Placeholder text for the text. Shown when the entry is locked.
            locked_image (str) -
                Placeholder text for the image. Shown when the entry is locked.
            locked_image_tint (tuple) -
                If no specific locked image is provided,
                a tinted version of the image will be used.
                The amount of tinting can be set with RGB values in a tuple.

        Attributes:
            has_image (bool): True if an image was provided, else False.
            pages (int): Number of pages this entry contains.

            has_sub_entry (bool): If an entry has any sub-entries.
        """
        def __init__(self,
                     parent=None,
                     number=None,  # type:  Optional[int]
                     name="",  # type: Optional[str]
                     text="",  # type: Optional[str]
                     subject="",  # type: Optional[str]
                     viewed=False,  # type: Optional[bool]
                     viewed_persistent=False,  # type: Optional[bool]
                     locked=False,  # type: Optional[bool]
                     locked_persistent=False,  # type: Optional[bool]
                     image=None,  # type: Optional[str]
                     locked_name="???",  # type: Optional[str]
                     locked_text="???",  # type: Optional[str]
                     locked_image=None,  # type: Optional[str]
                     locked_image_tint=(0.0, 0.0, 0.0)
                     ):
            # type: (...) -> None

            self.tint_locked_image = False
            # Place the entry into the assigned Encyclopaedia or EncEntry.

            # self.parent is set to None so that add_entry doesn't think
            # this EncEntry is already inside an Encyclopaedia.
            self.parent = None
            self.number = number

            self.locked_name = locked_name
            self.locked_text = string_to_list(locked_text)
            self.locked_image = locked_image

            self._name = name
            self._text = string_to_list(text)
            self._viewed = viewed
            self.subject = subject
            self._locked = locked
            self._image = image

            self.locked_persistent = locked_persistent
            if self.locked_persistent:
                self._locked = getattr(persistent, self._name + "_locked")

            if parent is not None:
                parent.add_entry(self)
                self.tint_locked_image = parent.tint_locked_image

            self.has_image = False
            if image is not None:
                self.has_image = True

                # If there's an image, but no locked image is specified,
                # tint the image and use it as the locked image.
                if locked_image is None and self.tint_locked_image:
                    # Tuple is used to set the numbers that tint_locked_image()
                    # uses to change the colour of a locked image
                    self.locked_image = enc_tint(
                        self._image, locked_image_tint
                    )

            self.pages = 1

            # List: The sub-entries and their position.
            #   The parent EncEntry must be the first in the sub-entry list.
            self.sub_entry_list = [[1, self]]

            self.has_sub_entry = False

            # Property: Set with Integer, get returns the page.
            self._current_page = 0

            self.callbacks = {
                "viewed": [],  # Run when this entry is viewed for the first time.
                "unlocked": [],  # Run when this entry is unlocked.
                "entry_unlocked": [],  # Run whenever a child entry is unlocked.
            }

            # When viewed is persistent, we get the viewed flag from persistent
            self.viewed_persistent = viewed_persistent
            if self.viewed_persistent:
                self._viewed = getattr(persistent, self._name + "_viewed")

        def __str__(self):  # type: () -> str
            return "EncEntry: {}".format(self.label)

        @property
        def locked(self):  # type: () -> bool
            """Determine if the entry's data can be viewed or not.
                Changing this variable will modify the entry's locked status.
            """
            return self._locked

        @locked.setter
        def locked(self, new_value):  # type: (bool) -> None
            if self.locked_persistent:
                setattr(persistent, self._name + "_locked", new_value)

            self._locked = new_value

            if self._locked is False:
                if isinstance(self.parent, EncEntry):
                    self.parent.add_entry(self)
                else:
                    self.parent.add_entry_to_unlocked_entries(self)

                self.parent.emit("entry_unlocked")
                self.emit("unlocked")

        @property
        def viewed(self):  # type: () -> bool
            """Determines if the entry has been viewed or not.
                Changing this variable will modify the entry's viewed status.
            """
            return self._viewed

        @viewed.setter
        def viewed(self, new_value):  # type: (bool) -> None
            if self.viewed_persistent:
                setattr(persistent, self._name + "_viewed", new_value)

            self._viewed = new_value

        @property
        def label(self):  # type: () -> str
            """The number and name of the entry, in the format of 'number: name'
            """
            return "{:02}: {}".format(self.number, self.name)

        @property
        def current_page(self):  # type: () -> EncEntry
            """Get the sub-page that's currently viewing viewed.
                Setting this attribute should be done using an integer.
            """
            return self.sub_entry_list[self._current_page][1]

        @current_page.setter
        def current_page(self, val):  # type: (int) -> None
            self._current_page = val - 1

        def __get_entry_data(self, data, locked_data):  # type: (Any, Any) -> Any
            """Used by self.name, self.text, and self.image to control if
            the locked placeholder or actual entry data should be returned.

            Returns:
                If True or None, return the data requested,
                otherwise the placeholder for the data
            """
            if self.locked or self.locked is None:
                return locked_data
            return data

        @property
        def name(self):  # type: () -> str
            """The name for the entry. Return placeholder when entry is locked."""
            return self.__get_entry_data(self._name, self.locked_name)

        @name.setter
        def name(self, val):  # type: (str) -> None
            self._name = val

            self.viewed = False

        @property
        def text(self):  # type: () -> list[str]
            """The text for the entry. Return placeholder when entry is locked."""
            return self.__get_entry_data(self._text, self.locked_text)

        @text.setter
        def text(self, val):  # type: (str) -> None
            self._text = val

            self.viewed = False

        @property
        def image(self):  # type: () -> str
            """The image for the entry. Return placeholder when entry is locked."""
            return self.__get_entry_data(self._image, self.locked_image)

        @image.setter
        def image(self, val):  # type: (str) -> None
            self.has_image = True
            self._image = val

            self.viewed = False

        def add_entry(self, entry):  # type: (EncEntry) -> bool
            """Adds multiple pages to the entry in the form of sub-entries.

            Args:
                entry: The entry to add as a sub-entry.

            Returns:
                bool: True if anything was added, else False
            """
            if entry.parent is not None and entry.parent != self:
                raise ValueError(
                    "{} is already a sub-page of another EncEntry".format(entry),
                )

            # When a new entry has a number, ensure it's not already used.
            if entry.number is not None:
                if any(i for i in self.sub_entry_list if i[1].number == entry.number):
                    raise ValueError(
                        "{} is already taken.".format(entry.number)
                    )

            elif entry.number is None:
                entry.number = self.pages + 1

            entry.parent = self

            if not [entry.number, entry] in self.sub_entry_list:
                if entry.locked is False:
                    self.sub_entry_list.append([entry.number, entry])
                    self.sub_entry_list = sorted(
                        self.sub_entry_list,
                        key=itemgetter(0)
                    )
                    self.has_sub_entry = True

                    self.pages = len(self.sub_entry_list)

                    return True
            return False

        @property
        def word_count(self):
            """Get the word count for the EncEntry's text.

            Returns:
                int
            """
            count = 0
            for item in self._text:
                count += len(item.split())
            return count

    from functools import partial



    def EncEntryTemplate(**kwargs):
        return partial(EncEntry, **kwargs)

    from math import floor
    import operator
    from operator import attrgetter




    class Encyclopaedia(EventEmitter, store.object):
        """Container that manages the behaviour of a collection of EncEntry objects.

        Args:
            sorting_mode (int): The type of sorting used.
                Default sorting is by Number.
            show_locked_buttons (bool): If True, locked entries show a
                placeholder label on the listing screen.
            show_locked_entry (bool): If True, locked entries can be viewed, but
                the data is hidden from view with a placeholder.
            entry_screen (str): The Ren'Py screen to display an open entry.

        Attributes:
            all_entries (list): All entries, regardless of status.
            unlocked_entries (list): Only unlocked entries.
            filtered_entries (list): Entries that match a subject filter.
            filtering (bool|str): The subject that's being used as a filter.
            size_all (int): Length of self.all_entries.
            size_unlocked (int): Length of self.unlocked_entries.
            reverse_sorting (bool): Should sorting occur in reverse or not.
            nest_alphabetical_sort (bool): Should alphabetical sorting display
                each letter as a subject.
            current_position (int): Index for the current entry open.
            sub_current_position (int): Index for the current sub-entry open.
                Starts at 1.
            labels (Labels): The current label controller.
            subjects (list): Collection of every subject.
            active (EncEntry): The currently open entry.
            locked_at_bottom (bool): If locked entries should appear at the bottom
                of the entry list or not.
        """
        # Constants for the different types of sorting available.
        SORT_NUMBER = 0
        SORT_ALPHABETICAL = 1
        SORT_REVERSE_ALPHABETICAL = 2
        SORT_SUBJECT = 3
        SORT_UNREAD = 4

        # Constants for the direction when scrolling through EncEntry.
        DIRECTION_FORWARD = 1
        DIRECTION_BACKWARD = -1

        # Used by check_position().
        operators = {'<=': operator.le, '>=': operator.ge}

        def __init__(self,
                     sorting_mode=0,  # type: (int)
                     show_locked_buttons=False,  # type: (bool)
                     show_locked_entry=False,  # type: (bool)
                     entry_screen="encyclopaedia_entry",  # type: (str)
                     tint_locked_image=True,  # type: (bool)
                     ):

            self.sorting_mode = sorting_mode
            self.default_sorting_mode = sorting_mode
            self.show_locked_buttons = show_locked_buttons
            self.show_locked_entry = show_locked_entry
            self.entry_screen = entry_screen

            self.tint_locked_image = tint_locked_image

            self.all_entries = []  # type: (List)
            self.unlocked_entries = []  # type: (List)
            self.filtered_entries = []  # type: (List)

            self.filtering = False

            self._size_all = 0
            self._size_unlocked = 0

            self.reverse_sorting = False
            if sorting_mode == self.SORT_REVERSE_ALPHABETICAL:
                self.reverse_sorting = True

            self.nest_alphabetical_sort = True

            self.current_position = 0
            self.sub_current_position = 1

            self.labels = Labels(self)

            self.subjects = []  # type: (List)

            self.active = None
            self._current_entries = self.all_entries

            self.locked_at_bottom = True

            self.callbacks = {
                "entry_unlocked": [],  # Run whenever a child entry is unlocked.
            }

        def __str__(self):  # type: () -> str
            return "Encyclopaedia: {} entries total".format(self._size_all)

        @property
        def current_entries(self):  # type: () -> List[EncEntry]
            """Depending on which viewing options are set,
            returns a list of entries.
            """
            if self.filtering:
                current_entries = self.filtered_entries
            elif self.show_locked_buttons:
                current_entries = self.all_entries
            else:
                current_entries = self.unlocked_entries

            return current_entries

        @current_entries.setter
        def current_entries(self, item):  # type: (List) -> None
            self._current_entries = item

        @property
        def percentage_unlocked(self):  # type: () -> float
            """Gets the percentage of the Encyclopaedia that's unlocked.

            Returns:
                float: Percentage of the Encyclopaedia that's unlocked

            Raises:
                ZeroDivisionError: If the Encyclopaedia is empty
            """
            float_size = float(self._size_unlocked)
            float_size_all = float(self._size_all)

            try:
                amount_unlocked = float_size / float_size_all
            except ZeroDivisionError:
                raise ZeroDivisionError(
                    'Cannot calculate percentage unlocked of empty Encyclopaedia'
                )

            percentage = floor(amount_unlocked * 100)
            return percentage

        @property
        def number_of_visible_entries(self):  # type: () -> int
            """Whatever the maximum size of the entry list should be,
            based on if locked entries should be shown or not.
            """
            if self.show_locked_entry:
                return self._size_all
            return self._size_unlocked

        def set_global_locked_name(self, placeholder):  # type: (str) -> None
            """Sets all the locked names for all entries to the same string.

            Args:
                placeholder (str): Text to use for every locked name
            """
            for item in self.all_entries:
                item.locked_name = placeholder

        def set_global_locked_image_tint(self, tint_amount):
            """Sets all the locked images for all entries to use the same tint.

            Args:
                tint_amount (tuple): An RGB value, ie:(R, G, B)
            """
            for item in self.all_entries:
                item[1].tint_locked_image(
                    (tint_amount[0], tint_amount[1], tint_amount[2])
                )

        def sort_entries(self, entries, sorting=0, reverse=False):
            """Sort entry lists by whatever the current sorting mode is.

            Args:
                entries (list): The entry list to sort
                sorting (int): The sorting mode to use
                reverse (bool): If the sorting should be done in reverse or not
            """
            if sorting == self.SORT_NUMBER:
                entries.sort(key=attrgetter('number'))
            else:
                entries.sort(reverse=reverse, key=attrgetter('name'))

                if sorting == self.SORT_UNREAD:
                    entries.sort(key=attrgetter('viewed'))

                elif sorting == self.SORT_SUBJECT:
                    entries.sort(key=attrgetter('subject'))

                if self.locked_at_bottom:
                    push_locked_to_bottom(entries)

        def check_position(self, op, position, wall):
            """Determines if the Prev/Next Actions should be active or not.

            Args:
                op (str): The operator to use
                position (int): The position of the entry
                wall (int): The limit to check against

            Returns:
                bool
            """
            if self.operators[op](position, wall):
                return True
            return False

        def add_entry_to_unlocked_entries(self, entry):
            """Add an entry to the list of unlocked entries.

            Args:
                entry (EncEntry): The Entry to add to the unlocked entries list.
            """

            self.unlocked_entries.append(entry)

            # Remove duplicates
            self.unlocked_entries = list(set(self.unlocked_entries))

            self.sort_entries(
                entries=self.unlocked_entries,
                sorting=self.sorting_mode,
                reverse=self.reverse_sorting
            )

            self._size_unlocked = len(self.unlocked_entries)

        def add_entry(self, entry):
            """Adds an entry to the Encyclopaedia's internal lists and sorts it.

            Attempts to create duplicates are softly ignored.
            subjects list is updated when a new entry is added.

            Args:
                entry (EncEntry): The Entry to add to the Encyclopaedia
            """
            if entry.parent is not None and entry.parent != self:
                raise ValueError(
                    "{} is already inside another Encyclopaedia".format(entry),
                )

            # When a new entry has a number, ensure it's not already used.
            if entry.number is not None:
                if any(i for i in self.all_entries if i.number == entry.number):
                    raise ValueError(
                        "{} is already taken.".format(entry.number)
                    )

            elif entry.number is None:
                if self._size_all > 0:
                    # All possible numbers
                    all_numbers = range(self.all_entries[-1].number + 1)[1:]
                    used_numbers = [item.number for item in self.all_entries]
                    free_numbers = set(all_numbers) - set(used_numbers)

                    if len(free_numbers) > 0:
                        # If there are unused numbers.
                        entry.number = min(free_numbers)
                    else:
                        # Else the entry is the last one.
                        entry.number = self._size_all + 1
                else:
                    # If there's no entries in the Encyclopaedia yet.
                    entry.number = 1

            self.all_entries.append(entry)
            entry.parent = self

            # Ensure no duplicates in the entry lists.
            self.all_entries = list(set(self.all_entries))

            # Ensure correct sorting of entry lists.
            self.sort_entries(
                entries=self.all_entries,
                sorting=self.sorting_mode,
                reverse=self.reverse_sorting
            )

            self._size_all = len(self.all_entries)

            if entry.locked is False:
                self.add_entry_to_unlocked_entries(entry)

            self.subjects.append(entry.subject)
            self.subjects = list(set(self.subjects))
            self.subjects.sort()

        @property
        def word_count(self):
            """Get the total word count for the Encyclopaedia.

            Returns:
                int
            """
            count = 0
            for entry in self.all_entries:
                count += entry.word_count
            return count

        def PreviousEntry(self):
            """Wrapper around an Action. Use with a renpy button.

            Returns:
                Screen Action
            """
            block = self.check_position(
                '<=',
                position=self.current_position,
                wall=0
            )

            return ChangeEntryAction(  # NOQA: F405
                encyclopaedia=self,
                direction=self.DIRECTION_BACKWARD,
                block=block
            )

        def NextEntry(self):
            """Wrapper around an Action. Use with a renpy button.

            Returns:
                Screen Action
            """
            block = self.check_position(
                '>=',
                position=self.current_position,
                wall=self.number_of_visible_entries - 1
            )

            return ChangeEntryAction(  # NOQA: F405
                encyclopaedia=self,
                direction=self.DIRECTION_FORWARD,
                block=block
            )

        def PreviousPage(self):
            """Wrapper around an Action. Use with a renpy button.

            Returns:
                Screen Action
            """
            block = self.check_position(
                '<=',
                position=self.sub_current_position,
                wall=1
            )

            return ChangePageAction(  # NOQA: F405
                encyclopaedia=self,
                direction=self.DIRECTION_BACKWARD,
                block=block
            )

        def NextPage(self):
            """Wrapper around an Action. Use with a renpy button.

            Returns:
                Screen Action
            """
            block = self.check_position(
                '>=',
                position=self.sub_current_position,
                wall=self.active.pages
            )

            return ChangePageAction(  # NOQA: F405
                encyclopaedia=self,
                direction=self.DIRECTION_FORWARD,
                block=block
            )

        def Sort(self, sorting_mode=None):  # NOQA: F405
            """Wrapper around an Action. Use with a renpy button.

            Args:
                sorting_mode: The type of sorting to use.
                    If None specified, use the current sorting.

            Returns:
                Screen Action
            """
            if sorting_mode is None:
                sorting_mode = self.sorting_mode

            return SortEncyclopaedia(self, sorting_mode)  # NOQA: F405

        def SetEntry(self, given_entry):
            """Wrapper around an Action. Use with a renpy button.

            Returns:
                Screen Action
            """
            return SetEntryAction(self, given_entry)  # NOQA: F405

        def ResetSubPage(self):
            """Wrapper around an Action. Use with a renpy button.

            Returns:
                Screen Action
            """
            return ResetSubPageAction(self)  # NOQA: F405

        def ToggleShowLockedButtons(self):
            """Wrapper around an Action. Use with a renpy button.

            Returns:
                Screen Action
            """
            return ToggleShowLockedButtonsAction(self)  # NOQA: F405

        def ToggleShowLockedEntry(self):
            """Wrapper around an Action. Use with a renpy button.

            Returns:
                Screen Action
            """
            return ToggleShowLockedEntryAction(self)  # NOQA: F405

        def FilterBySubject(self, subject):
            """Wrapper around an Action. Use with a renpy button.

            Returns:
                Screen Action
            """
            return FilterBySubject(self, subject)  # NOQA: F405

        def ClearFilter(self):
            """Wrapper around an Action. Use with a renpy button.

            Returns:
                Screen Action
            """
            return ClearFilter(self)  # NOQA: F405

    from operator import attrgetter


    def push_locked_to_bottom(seq):
        """Moves all the locked entries in a list of entries to
        the bottom of the list.

        Args:
            seq: The sequence of EncEntry to sort.

        Returns:
            list: Sorted version of the given sequence
        """
        new_list = sorted(seq, reverse=True, key=attrgetter('locked'))

        del seq[:]

        for item in new_list:
            seq.append(item)

        return seq



    class Labels(store.object):
        """Controls how the labels that display Encyclopaedia data appear.

        Attributes:
            percentage_label (str): Placed next to the percentage unlocked number
            page_label (str): Placed before the entry page displayed
            page_separator_label (str): Placed in-between the
                current page number and the total page number

            sort_number_label (str): Label for Number Sorting
            sort_alphabetical_label (str): Label for Alphabetical sorting
            sort_reverse_alphabetical_label (str): Label for Reverse Alphabetical
                sorting
            sort_subject_label (str): Label for Subject sorting
            sort_unread_label (str): Label for Unread sorting

            unread_entry_label (str): Default for the tag next to unread entries
            locked_entry_label (str): Default for a "Locked Entry" button
        """
        def __init__(self, encyclopaedia):  # type: (Encyclopaedia) -> None
            self.encyclopaedia = encyclopaedia

            self.percentage_label = '%'
            self.page_label = 'Page'
            self.page_separator_label = '/'

            self.sort_number_label = "Number"
            self.sort_alphabetical_label = "A to Z"
            self.sort_reverse_alphabetical_label = "Z to A"
            self.sort_subject_label = "Subject"
            self.sort_unread_label = "Unread"

            self.unread_entry_label = "New!"
            self.locked_entry_label = "???"

        @property
        def percentage_unlocked(self):  # type: () -> str
            """Percentage representation of the amount of the encyclopaedia
            that's unlocked. ie: '50%'.

            Returns:
                str
            """
            percentage_unlocked = int(self.encyclopaedia.percentage_unlocked)
            return "{}{}".format(percentage_unlocked, self.percentage_label)

        @property
        def entry_current_page(self):  # type: () -> str
            """The sub-page of an entry that is being viewed.

            Returns:
                str
            """
            try:
                total_pages = self.encyclopaedia.active.pages
            except AttributeError:
                raise AttributeError(
                    "Cannot display Entry's current page when no entry is open."
                )

            label = "{0} {1} {2} {3}".format(
                self.page_label,
                self.encyclopaedia.sub_current_position,
                self.page_separator_label,
                total_pages
            )

            return label

        @property
        def sorting_mode(self):  # type: () -> str
            """Label for the encyclopaedia's current sorting mode.

            Returns:
                str
            """
            enc = self.encyclopaedia

            sorting_strings = {
                enc.SORT_NUMBER: self.sort_number_label,
                enc.SORT_ALPHABETICAL: self.sort_alphabetical_label,
                enc.SORT_REVERSE_ALPHABETICAL: self.sort_reverse_alphabetical_label,  # NOQA: E501
                enc.SORT_SUBJECT: self.sort_subject_label,
                enc.SORT_UNREAD: self.sort_unread_label
            }

            return sorting_strings[enc.sorting_mode]

    from renpy.python import RevertableList


    def enc_tint(image, tint_amount):
        """Tint an image.

        If the EncEntry has an image but no locked image, tint the image
        and use it as the locked image.

        Args:
            image: The image to tint
            tint_amount: Tuple for the RGB values to tint the image

        Returns:
            tinted image
        """

        matrix = im.matrix.tint(
            tint_amount[0],
            tint_amount[1],
            tint_amount[2],
        )

        tinted_image = im.MatrixColor(
            image,
            matrix,
        )

        return tinted_image


    def string_to_list(given_text):  # type: (Optional[str, List]) -> List
        """Turn a string into a list containing that string.

        Each list item represents a paragraph.
        If a string is given, convert it to a list,
        assuming a string with no list = one paragraph.

        Args:
            given_text [str|list]

        Returns:
            list
        """
        # If the text is already in a list, just return it.
        if type(given_text) in (RevertableList, list):
            return given_text
        return [given_text]
