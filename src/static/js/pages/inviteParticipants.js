/*global ParticipantsAutocompleteView InvitedGroupController FilterModalView FilterModalController ThemeAutocompleteView GroupAutocompleteView */

var participantsAutocompleteView = new ParticipantsAutocompleteView();
participantsAutocompleteView.initEvents();

var invitedGroupController = new InvitedGroupController();
invitedGroupController.initEvents();

var filterModalView = new FilterModalView();
filterModalView.initEvents();

var filterModalController = new FilterModalController();
filterModalController.initEvents();

var themeAutocompleteView = new ThemeAutocompleteView();
themeAutocompleteView.initEvents();

var groupAutocompleteView = new GroupAutocompleteView();
groupAutocompleteView.initEvents();
