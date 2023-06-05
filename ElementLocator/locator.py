class elem():
    username = "input[name='username']"
    password = "input[name='password']"
    loginButton = "orangehrm-login-button"
    errorMessage = ".oxd-text.oxd-text--span.oxd-input-field-error-message.oxd-input-group__message"
    profilAvatar = '.oxd-userdropdown-tab'
    logoutButton = ':nth-child(4) > .oxd-userdropdown-link'
    loginTitle = '.oxd-text--h5'
    loginForm = '.orangehrm-login-form'
    resetPasswordTitle = '.oxd-text--h6'
    forgotPasswordButton = '.orangehrm-login-forgot > .oxd-text'
    adminButton = ':nth-child(1) > .oxd-main-menu-item'
    addUserButton = '.orangehrm-header-container > .oxd-button'

    recordsFoundText = '.orangehrm-horizontal-padding'
    userManagementButton = '.--visited > .oxd-topbar-body-nav-tab-item'
    usersTableBody = '.oxd-table-body'
    usersCellEditButton = ':nth-child(1) > .oxd-table-row > :nth-child(6) > .oxd-table-cell-actions > :nth-child(2) > .oxd-icon'
    usersCellDeleteButton = ':nth-child(2) > .oxd-table-row > :nth-child(6) > .oxd-table-cell-actions > :nth-child(1) > .oxd-icon'
    addUserTitle = '.orangehrm-card-container > .oxd-text--h6'
    userRoleDropdown = ':nth-child(1) > .oxd-input-group > :nth-child(2) > .oxd-select-wrapper > .oxd-select-text > .oxd-select-text--after > .oxd-icon'
    statusDropdown = ':nth-child(3) > .oxd-input-group > :nth-child(2) > .oxd-select-wrapper > .oxd-select-text > .oxd-select-text--after > .oxd-icon'
    employeeNameInput = ':nth-child(3) > .oxd-input-group > :nth-child(2) > .oxd-select-wrapper > .oxd-select-text > .oxd-select-text--after > .oxd-icon'
    userNameInput = ':nth-child(4) > .oxd-input-group > :nth-child(2) > .oxd-input'
    passwordInput = '.user-password-cell > .oxd-input-group > :nth-child(2) > .oxd-input'
    confirmPasswordInput = ':nth-child(2) > .oxd-input-group > :nth-child(2) > .oxd-input'
    usersSaveBtn = '.oxd-button--secondary'
    usersCancelBtn = '.oxd-button--ghost'
    editUserPageTitle = '.orangehrm-card-container > .oxd-text--h6'
    userDeleteConfirmationYesButton = '.oxd-button--label-danger'
    userDeleteConfirmationTitle = '.orangehrm-modal-header > .oxd-text'
    userDeleteConfirmationNoButton = '.oxd-button--text'
    pimBtn = "/html[1]/body[1]/div[1]/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[2]/a[1]"
    pimModule = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/h5[1]"
    fieldEmployee = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]"
    btnSearch = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[2]/button[2]"
    checkboxSearch = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/label[1]/span[1]/i[1]"
    btnDeleteSection = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/button[1]"
    btnModalDeleteSection = "/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[3]/button[2]"
    pimDeleteToast = "oxd-toaster_1"
    btnEditPIM = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[9]/div[1]/button[2]/i[1]"
    btnSaveEditPIM = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/form[1]/div[2]/button[1]"
    pimSuccessEditToast = "oxd-toaster_1"
    btnSubMenuJob = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[6]/a[1]"
    btnSubMenuSalary = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[7]/a[1]"
    fieldJoinedDate = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]"
    fieldJobCategory = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]"
    fieldEmploymentStatus = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[7]/div[1]/div[2]/div[1]/div[1]/div[1]"
    fieldJobTitle = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[7]/div[1]/div[2]/div[1]/div[1]/div[1]"
    btnSaveJob = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/button[1]"
    btnEditSalary = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[7]/div[1]/button[2]/i[1]"
    fieldSalaryComponents = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]"
    fieldAmount = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[5]/div[1]/div[2]/input[1]"
    


    userDeleteToast = '.oxd-text--toast-message'

    # Add user form
    roleEssOption = '.oxd-select-dropdown > :nth-child(3) > span'
    statusEnabledOption = '.oxd-select-dropdown > :nth-child(2) > span'


    employeeNameInput = '.oxd-autocomplete-text-input > input'
    usernameInput = ':nth-child(4) > .oxd-input-group > :nth-child(2) > .oxd-input'
    passwordInput = '.user-password-cell > .oxd-input-group > :nth-child(2) > .oxd-input'
    confirmPasswordInput = ':nth-child(2) > .oxd-input-group > :nth-child(2) > .oxd-input'
    addUserSaveButton = '.oxd-button--secondary'
    addUserCancelButton = '.oxd-button--secondary'
    employeeNameOption = '.oxd-autocomplete-dropdown > :nth-child(4)'
    addUserToastMessage = '.oxd-text--toast-message'

    # edit user
    editUsernameInput = ':nth-child(2) > .oxd-input'

    editUserToastMessage = '.oxd-text--toast-message'
    editSaveButton = '/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[2]/button[2]'

    requiredNote = '.oxd-form-actions > .oxd-text'

