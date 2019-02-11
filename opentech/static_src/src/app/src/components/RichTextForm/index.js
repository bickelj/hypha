import React from 'react';
import PropTypes from 'prop-types';
import RichTextEditor from 'react-rte';

const toolbarConfig = {
    display: ['INLINE_STYLE_BUTTONS', 'BLOCK_TYPE_BUTTONS', 'BLOCK_TYPE_DROPDOWN', 'LINK_BUTTONS'],
    INLINE_STYLE_BUTTONS: [
        {label: 'Bold', style: 'BOLD', className: 'custom-css-class'},
        {label: 'Italic', style: 'ITALIC'},
        {label: 'Underline', style: 'UNDERLINE'},
        {label: 'Blockquote', style: 'blockquote'},

    ],
    BLOCK_TYPE_DROPDOWN: [
        {label: 'Normal', style: 'unstyled'},
        {label: 'H1', style: 'header-four'},
        {label: 'H2', style: 'header-five'},
    ],
    BLOCK_TYPE_BUTTONS: [
        {label: 'UL', style: 'unordered-list-item'},
        {label: 'OL', style: 'ordered-list-item'}
    ]
};

export default class RichTextForm extends React.Component {
    static defaultProps = {
        disabled: false,
        initialValue: '',
    };

    static propTypes = {
        disabled: PropTypes.bool.isRequired,
        onValueChange: PropTypes.func,
        value: PropTypes.string,
        instance: PropTypes.string,
        onSubmit: PropTypes.func,
    };

    state = {
        value: RichTextEditor.createEmptyValue(),
    };

    resetEditor = () => {
        this.setState({value: RichTextEditor.createEmptyValue()});
    }

    render() {
        const { instance, disabled } = this.props;

        return (
            <div className={ instance } >
                <RichTextEditor
                    disabled={ disabled }
                    onChange={ this.handleValueChange }
                    value={ this.state.value }
                    className="add-note-form__container"
                    toolbarClassName="add-note-form__toolbar"
                    editorClassName="add-note-form__editor"
                    toolbarConfig={toolbarConfig}
                />
                <button
                    disabled={this.isEmpty() || disabled}
                    onClick={this.handleSubmit}
                    className={`button ${instance}__button`}
                >
                    Submit
                </button>
            </div>
        );
    }

    isEmpty = () => {
        return !this.state.value.getEditorState().getCurrentContent().hasText();
    }

    handleValueChange = value => {
        this.setState({value});
    }

    handleSubmit = () => {
        this.props.onSubmit(this.state.value.toString('html'), this.resetEditor);
    }
}